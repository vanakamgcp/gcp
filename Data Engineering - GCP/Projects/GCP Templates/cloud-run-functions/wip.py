import json
import logging
from google.cloud import bigquery

def load_json_to_bigquery(file_path, dataset_id, table_id):
    """Reads a JSON file and loads it into a BigQuery table."""
    try:
        # Initialize BigQuery client
        client = bigquery.Client()

        # Read the JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Define the table reference
        table_ref = client.dataset(dataset_id).table(table_id)

        # Insert data into BigQuery
        errors = client.insert_rows_json(table_ref, data)
        if errors:
            logging.error(f"Errors occurred while inserting rows: {errors}")
        else:
            logging.info("Data loaded successfully into BigQuery.")
    except Exception as e:
        logging.error(f"Failed to load data into BigQuery: {e}")

if __name__ == "__main__":
    # Replace these variables with your actual values
    FILE_PATH = "/Users/ajithkumarj/coder_mode/gcp/Data Engineering - GCP/Projects/GCP Templates/cloud-run-functions/json-load-bq/sample_data/employees.json"
    DATASET_ID = "your_bigquery_dataset"
    TABLE_ID = "your_bigquery_table"

    load_json_to_bigquery(FILE_PATH, DATASET_ID, TABLE_ID)