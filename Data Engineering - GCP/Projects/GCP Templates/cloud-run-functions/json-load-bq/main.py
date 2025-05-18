import json
import logging
import os
from google.cloud import storage, bigquery
from google.api_core.exceptions import GoogleAPIError
from tenacity import retry, stop_after_attempt, wait_exponential

# Configure logging
logging.basicConfig(level=logging.INFO)

# Retry configuration
@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
def download_json_from_gcs(bucket_name, source_blob_name):
    """Download a JSON file from GCS."""
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(source_blob_name)
        data = blob.download_as_text()
        logging.info(f"File {source_blob_name} downloaded from bucket {bucket_name}.")
        return json.loads(data)
    except GoogleAPIError as e:
        logging.error(f"Error downloading file from GCS: {e}")
        return None

def transform_data(data):
    """Transform the data. Modify this function for specific transformations."""
    try:
        # # Example transformation: Add a new field to each record
        # for record in data:
        #     record['processed'] = True
        logging.info("Data transformation completed.")
        return data
    except Exception as e:
        logging.error(f"Error during data transformation: {e}")
        raise

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
def load_data_to_bigquery(data, dataset_id, table_id):
    """Load data into BigQuery."""
    try:
        client = bigquery.Client()
        table_ref = client.dataset(dataset_id).table(table_id)
        job_config = bigquery.LoadJobConfig(
            schema = [
                bigquery.SchemaField("EMPLOYEE_ID", "STRING"),
                bigquery.SchemaField("FIRST_NAME", "STRING"),
                bigquery.SchemaField("LAST_NAME", "STRING"),
                bigquery.SchemaField("EMAIL", "STRING"),
                bigquery.SchemaField("PHONE_NUMBER", "STRING"),
                bigquery.SchemaField("HIRE_DATE", "STRING"),
                bigquery.SchemaField("JOB_ID", "STRING"),
                bigquery.SchemaField("SALARY", "NUMERIC"),
                bigquery.SchemaField("COMMISSION_PCT", "NUMERIC"),
                bigquery.SchemaField("MANAGER_ID", "STRING"),
                bigquery.SchemaField("DEPARTMENT_ID", "STRING"),
            ],
            source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
            write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
        )
        job = client.load_table_from_json(data, table_ref, job_config=job_config)
        job.result()  # Wait for the job to complete
        logging.info(f"Data loaded into BigQuery table {dataset_id}.{table_id}.")
    except GoogleAPIError as e:
        logging.error(f"Error loading data to BigQuery: {e}")
        raise

def main(bucket_name, source_blob_name, dataset_id, table_id):
    """Main function to orchestrate the process."""
    try:
        # Step 1: Download JSON from GCS
        data = download_json_from_gcs(bucket_name, source_blob_name)

        # Step 2: Transform the data
        transformed_data = transform_data(data)

        # Step 3: Load data into BigQuery
        load_data_to_bigquery(transformed_data, dataset_id, table_id)

        logging.info("Process completed successfully.")
    except Exception as e:
        logging.error(f"Process failed: {e}")
    
