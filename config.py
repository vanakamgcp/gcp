import os

# Configuration for GCS to BigQuery Load Job
JOB_NAME = "gcs_to_bq_raw_load"
DATASET_NAME = "ds_raw_feb26"
TABLE_NAME = "employees"
FILE_FORMAT = "CSV"
LOAD_TYPE = "WRITE_APPEND"

# GCS Buckets
LANDING_BUCKET = "gcs_feb26_land_bkt"
ARCHIVE_BUCKET = "gcs_feb26_arch_bkt"
ERROR_BUCKET = "gcs_feb26_err_bkt"

# Validation Rules
FILE_NAME_PATTERN = r"employees_(\d{8})\.csv"
MANDATORY_NON_NULL_COLUMNS = ["EMPLOYEE_ID"]
CSV_DELIMITER = ","
HAS_HEADER = True

# BigQuery Load Config
BQ_LOAD_CONFIG = {
    "skip_leading_rows": 1 if HAS_HEADER else 0,
    "field_delimiter": CSV_DELIMITER,
    "autodetect": False,  # Strict constraint: use existing table schema as source of truth
    "write_disposition": "WRITE_APPEND"
}