# GCS to BigQuery One-Time Migration Framework

This repository contains a lightweight and cost-effective framework to facilitate **one-time migration** of structured data from **Google Cloud Storage (GCS)** to **BigQuery**. It is specifically designed for initial table creation and loading, leveraging **Cloud Run**, **Cloud Functions**, and **GCP Workflows** for high-performance, parallel execution.

---

## 🚀 Overview

This framework is built to:
- Read data files from a GCS bucket.
- Map each folder within the bucket to a corresponding BigQuery table.
- Load the data into BigQuery using a scalable, serverless architecture.
- Execute the process in parallel for faster table creation.

This is ideal for initial setup or bootstrapping of datasets into a BigQuery data warehouse.

---

## 🧱 Architecture

- **Google Cloud Storage (GCS)**: Source of raw data files. Each folder = one table.
- **Google Cloud Workflows**: Orchestrates the parallel execution of table creation jobs.
- **Cloud Run / Cloud Functions**: Stateless services to handle individual table ingestion logic.
- **BigQuery**: Destination for table creation and data loading.


### 📁 Folder Structure Example

- `gs://your-bucket-name/`
  - `customers/`
    - `data1.csv`
    - `data2.csv`
  - `orders/`
    - `part1.csv`
  - `transactions/`
    - `tx1.csv`
    - `tx2.csv`


Each folder contains data files (e.g., CSV, JSON, Avro) representing a table in BigQuery.

---

## ⚙️ How It Works

1. **Trigger**: Migration can be manually triggered or automated.
2. **Workflow Orchestration**:
   - GCP Workflows reads all folder names in the bucket.
   - Launches parallel executions (Cloud Run/Functions) for each folder.
3. **Table Creation & Load**:
   - Services fetch the relevant data.
   - Schema is auto-detected or manually provided.
   - Data is loaded into BigQuery tables under a specified dataset.

---

## ✅ Benefits

- **High Performance**: Parallel execution of table loads reduces total runtime.
- **Serverless Architecture**: Cloud-native, fully managed, no infrastructure overhead.
- **Cost-Effective**: Pay-per-use model with minimal operational cost.
- **Modular & Maintainable**: Easy to extend or integrate into larger data pipelines.
- **One-Time Use**: Meant only for initial migration — future ingestion can use separate pipelines.

---

## 📦 Use Case Example

You're tasked with migrating historical data for 50+ tables, each stored in a folder within a GCS bucket. Instead of writing custom ingestion logic for each, simply run the workflow. It detects all folders and runs parallel jobs to load data into BigQuery — saving hours of effort and ensuring consistency.

---

## 🛠️ Tech Stack

- Google Cloud Storage (GCS)
- Google Cloud Workflows
- Google Cloud Functions or Cloud Run
- BigQuery

---

## 📌 Notes

- This framework is **not intended** for recurring or incremental loads.
- Folder naming in GCS must match the intended BigQuery table names.
- Ensure necessary IAM permissions are granted to allow storage access and BigQuery write operations.

---

## 📄 License

MIT License. See `LICENSE` file for details.
