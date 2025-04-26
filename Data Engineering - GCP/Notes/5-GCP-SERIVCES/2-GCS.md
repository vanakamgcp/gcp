# Google Cloud Storage (GCS)

Google Cloud Storage (GCS) is a scalable, fully-managed object storage service for unstructured data. It is designed for durability, availability, and performance, making it suitable for a wide range of use cases such as data lakes, backups, and content delivery.

## Types of Storage Classes

GCS offers four storage classes optimized for different use cases:

1. **Standard Storage**  
    - Best for frequently accessed ("hot") data.  
    - Use cases: Websites, mobile apps, and analytics.  

2. **Nearline Storage**  
    - Best for infrequently accessed data (accessed less than once a month).  
    - Use cases: Backups and long-tail multimedia content.  

3. **Coldline Storage**  
    - Best for rarely accessed data (accessed less than once a year).  
    - Use cases: Disaster recovery and archival storage.  

4. **Archive Storage**  
    - Best for long-term storage of rarely accessed data.  
    - Use cases: Regulatory archives and long-term backups.  

## Storage Costs

Costs vary based on the storage class and operations performed. Below is a general overview:

| Storage Class      | Storage Cost (per GB/month) | Retrieval Cost (per GB) |
|---------------------|-----------------------------|--------------------------|
| Standard Storage    | Higher                     | None                     |
| Nearline Storage    | Lower                      | Moderate                 |
| Coldline Storage    | Lower                      | Higher                   |
| Archive Storage     | Lowest                     | Highest                  |

> **Note:** Additional costs may apply for operations, network egress, and data replication.

## IAM Roles and Permissions

To manage access to GCS, you can use predefined IAM roles or create custom roles. Below are some common predefined roles:

- **Storage Admin (`roles/storage.admin`)**  
  Full control over GCS resources.

- **Storage Object Admin (`roles/storage.objectAdmin`)**  
  Full control over objects, but no control over buckets.

- **Storage Object Creator (`roles/storage.objectCreator`)**  
  Permission to upload objects, but not delete them.

- **Storage Object Viewer (`roles/storage.objectViewer`)**  
  Read-only access to objects.

### Permissions

Permissions are granular actions that IAM roles grant. Examples include:

- `storage.buckets.create` – Create buckets.  
- `storage.objects.get` – Read objects.  
- `storage.objects.delete` – Delete objects.  

## Additional Resources

- [GCS Documentation](https://cloud.google.com/storage/docs)  
- [Pricing Details](https://cloud.google.com/storage/pricing)  
- [IAM Roles and Permissions](https://cloud.google.com/iam/docs/understanding-roles)  
## Real-Time Examples for Data Migration

Here are some real-world scenarios where GCS is used for data migration:

1. **On-Premises to GCS**  
    - Use the `gsutil` command-line tool or the Storage Transfer Service to migrate data from on-premises storage to GCS.  
    - Example: A company migrating its legacy file server data to GCS for better scalability and durability.

2. **Cloud-to-Cloud Migration**  
    - Transfer data from another cloud provider (e.g., AWS S3) to GCS using the Storage Transfer Service.  
    - Example: A business moving its analytics data from AWS S3 to GCS to integrate with BigQuery.

3. **Database Backups to GCS**  
    - Export database backups (e.g., MySQL, PostgreSQL) to GCS for disaster recovery or archival purposes.  
    - Example: A SaaS provider storing daily database backups in GCS Archive Storage for long-term retention.

4. **Streaming Data to GCS**  
    - Use tools like Apache Beam or Dataflow to stream real-time data into GCS for processing or storage.  
    - Example: A media company streaming user activity logs to GCS for analytics.

5. **Hybrid Cloud Solutions**  
    - Synchronize data between on-premises systems and GCS for hybrid cloud setups.  
    - Example: A retail company syncing product images from its local servers to GCS for global distribution.

> **Tip:** Use appropriate storage classes based on the frequency of access and retention requirements during migration.