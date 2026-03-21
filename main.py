import uuid
import json
import sys
from datetime import datetime
from google.cloud import storage, bigquery

import config
from utils.logger import get_logger, log_process_step
from utils import gcs_utils as gcs
from utils import bq_utils as bq

logger = get_logger(config.JOB_NAME)

def capture_final_metrics(batch_id, file_name, file_row_count, rows_loaded, start_time, job_status, error_message):
    """
    Captures final job metrics and prints them in a plain JSON format.
    """
    metrics = {
        "job_name": config.JOB_NAME,
        "batch_id": batch_id,
        "file_name": file_name if file_name else "N/A",
        "file_row_count": file_row_count,
        "start_time": start_time.isoformat(),
        "end_time": datetime.utcnow().isoformat(),
        "rows_loaded": rows_loaded,
        "job_status": job_status,
        "error_message": error_message if error_message else "N/A"
    }
    print(json.dumps(metrics))
    return metrics

def run_pipeline(request=None):
    # Initialize Job Constants
    batch_id = str(uuid.uuid4())
    start_time = datetime.utcnow()
    job_status = "FAILED"
    error_message = None
    file_name = None
    file_row_count = 0
    rows_loaded = 0
    
    storage_client = storage.Client()
    bq_client = bigquery.Client()

    try:
        log_process_step("Script started", details=f"Batch ID: {batch_id}")

        # 1. List files in landing bucket
        log_process_step("File validation started")
        blobs = list(storage_client.list_blobs(config.LANDING_BUCKET))
        
        if not blobs:
            logger.info("No files found in landing bucket. Exiting.")
            job_status = "SUCCESS" # No file to process is not a failure
            return {"status": "SUCCESS", "message": "No files found in landing bucket"}, 200
            
        if len(blobs) > 1:
            raise Exception(f"Validation Error: Multiple files allowed per execution: NO. Found {len(blobs)}.")
        
        blob = blobs[0]
        file_name = blob.name
        
        # 2. Validate File (Pattern, Date, Empty)
        is_valid, msg, date_str = gcs.validate_file(blob, config.FILE_NAME_PATTERN)
        if not is_valid:
            raise Exception(f"File Validation Failed: {msg}")
        
        log_process_step("File validation completed", status="SUCCESS")

        # 3. Validate Data (Mandatory columns and NULL checks)
        log_process_step("Data validation started")
        is_valid, msg, file_row_count = gcs.validate_data(blob, config.MANDATORY_NON_NULL_COLUMNS)
        if not is_valid:
            raise Exception(f"Data Validation Failed: {msg}")
        
        log_process_step("Data validation completed", status="SUCCESS", details=f"Row count: {file_row_count}")

        # 4. Load to BigQuery
        log_process_step("BigQuery load started")
        gcs_uri = f"gs://{config.LANDING_BUCKET}/{file_name}"
        
        rows_loaded = bq.load_to_bigquery(
            bq_client, 
            gcs_uri, 
            config.DATASET_NAME, 
            config.TABLE_NAME, 
            config.BQ_LOAD_CONFIG
        )
        
        # 5. Row count validation (Threshold 0)
        if rows_loaded != file_row_count:
            raise Exception(f"Row count mismatch! Source file: {file_row_count}, BQ Loaded: {rows_loaded}")
            
        log_process_step("BigQuery load completed", status="SUCCESS", details=f"Rows loaded: {rows_loaded}")

        # 6. File Movement (SUCCESS -> Archive)
        log_process_step("File movement started")
        dest_path = gcs.move_file(storage_client, config.LANDING_BUCKET, file_name, config.ARCHIVE_BUCKET, "SUCCESS")
        log_process_step("File movement completed", status="SUCCESS", details=f"Moved to: {dest_path}")

        job_status = "SUCCESS"
        log_process_step("Script finished", status="SUCCESS")

    except Exception as e:
        job_status = "FAILED"
        error_message = str(e)
        logger.error(f"Job Critical Error: {error_message}")
        
        # File Movement (FAILURE -> Error)
        if file_name:
            try:
                log_process_step("File movement started (Error path)")
                dest_path = gcs.move_file(storage_client, config.LANDING_BUCKET, file_name, config.ERROR_BUCKET, "FAILED")
                log_process_step("File movement completed (Error path)", status="FAILED", details=f"Moved to: {dest_path}")
            except Exception as move_err:
                logger.error(f"Failed to move file to error bucket: {str(move_err)}")

    finally:
        # Capture and Log Metrics
        metrics = capture_final_metrics(
            batch_id, 
            file_name, 
            file_row_count, 
            rows_loaded, 
            start_time, 
            job_status, 
            error_message
        )
        
        if job_status == "FAILED":
            # Keep sys.exit(1) logic for failures while ensuring some return for the path that doesn't exit
            sys.exit(1)
        
        return metrics, 200

if __name__ == "__main__":
    run_pipeline()
