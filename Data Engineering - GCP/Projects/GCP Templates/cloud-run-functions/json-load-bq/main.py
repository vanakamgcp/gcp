from google.cloud import bigquery, storage
from google.api_core.exceptions import GoogleAPIError
from datetime import datetime
import pandas as pd
import json
import io


def load_and_process_json_to_bigquery(
    gcs_bucket: str,
    gcs_blob_path: str,
    dataset_id: str,
    table_id: str,
    project_id: str,
    write_disposition: str = "WRITE_APPEND"
) -> dict:
    """
    Reads JSON from GCS, processes it, and loads it into BigQuery.

    Returns:
        dict: Audit info including job status, row count, errors, timings.
    """

    job_start = datetime.now()
    audit_output = {
        "job_start_time": job_start,
        "job_end_time": None,
        "row_count": 0,
        "status": "FAILED",
        "error": None,
        "source_uri": f"gs://{gcs_bucket}/{gcs_blob_path}",
        "target_table": f"{project_id}.{dataset_id}.{table_id}",
    }

    try:
        # Step 1: Read file from GCS
        storage_client = storage.Client(project=project_id)
        bucket = storage_client.bucket(gcs_bucket)
        blob = bucket.blob(gcs_blob_path)
        file_content = blob.download_as_text()

        # Step 2: Parse and process JSON
        json_records = [json.loads(line) for line in file_content.strip().splitlines()]
        df = pd.DataFrame(json_records)

        # 🔧 Step 3: Process Data - PLACEHOLDER for custom logic
        # Example: Drop nulls and filter
        df.dropna(subset=["important_column"], inplace=True)
        df = df[df["status"] == "active"]

        # Step 4: Load to BigQuery
        bq_client = bigquery.Client(project=project_id)
        job_config = bigquery.LoadJobConfig(
            write_disposition=write_disposition,
            autodetect=True,
        )

        job = bq_client.load_table_from_dataframe(
            df,
            destination=f"{project_id}.{dataset_id}.{table_id}",
            job_config=job_config
        )
        job.result()  # Wait for job to finish

        audit_output["row_count"] = len(df)
        audit_output["status"] = "SUCCESS"

    except GoogleAPIError as api_err:
        audit_output["error"] = str(api_err)
    except Exception as e:
        audit_output["error"] = str(e)

    job_end = datetime.utcnow()
    audit_output["job_end_time"] = job_end.isoformat()

    return audit_output
