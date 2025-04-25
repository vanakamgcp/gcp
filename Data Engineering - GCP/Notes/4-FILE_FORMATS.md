# File Formats for Data Migration

## 1. CSV (Comma-Separated Values)
### Description:
- Plain text format where data is separated by commas.
- Easy to read and write.
- Supported by most tools and programming languages.

### Advantages:
- Human-readable.
- Lightweight and simple.

### Disadvantages:
- No support for complex data types.
- No schema enforcement.
- Larger file size compared to binary formats.

### Use Cases:
- Simple data exchange between systems.
- Small datasets.
- When human readability is required.

---

## 2. JSON (JavaScript Object Notation)
### Description:
- Text-based format for structured data.
- Supports nested and hierarchical data.

### Advantages:
- Human-readable.
- Supports complex data structures.
- Widely used in APIs and web applications.

### Disadvantages:
- Larger file size compared to binary formats.
- Parsing can be slower for large datasets.

### Use Cases:
- Data with nested structures.
- Web applications and APIs.
- Interoperability between systems.

---

## 3. PARQUET
### Description:
- Columnar storage format optimized for analytical workloads.
- Developed by Apache.

### Advantages:
- Highly efficient for read-heavy operations.
- Supports schema evolution.
- Compression reduces storage costs.

### Disadvantages:
- Not human-readable.
- Slower for write-heavy operations.

### Use Cases:
- Big data analytics.
- Data warehousing.
- Querying specific columns in large datasets.

---

## 4. ORC (Optimized Row Columnar)
### Description:
- Columnar storage format optimized for Hadoop ecosystems.
- Developed by Apache.

### Advantages:
- High compression ratio.
- Optimized for read-heavy operations.
- Supports schema evolution.

### Disadvantages:
- Not human-readable.
- Slower for write-heavy operations.

### Use Cases:
- Hadoop-based data processing.
- Big data analytics.
- Data warehousing.

---

## 5. AVRO
### Description:
- Row-based storage format with schema support.
- Developed by Apache.

### Advantages:
- Compact and efficient.
- Schema is embedded in the file.
- Supports schema evolution.

### Disadvantages:
- Not human-readable.
- Parsing requires schema.

### Use Cases:
- Data serialization.
- Streaming data pipelines.
- Interoperability between systems.

---

## 6. XML (eXtensible Markup Language)
### Description:
- Text-based format for structured data.
- Uses tags to define elements and hierarchy.

### Advantages:
- Human-readable.
- Supports nested and hierarchical data.
- Extensible and flexible.

### Disadvantages:
- Verbose and larger file size.
- Parsing can be slower compared to other formats.

### Use Cases:
- Data exchange in legacy systems.
- Configuration files.
- Documents requiring strict validation.

---

## Updated Summary of Use Cases
| File Format | Best For                          |
|-------------|-----------------------------------|
| CSV         | Simple, small datasets           |
| JSON        | Nested, hierarchical data        |
| PARQUET     | Analytical workloads, big data   |
| ORC         | Hadoop-based analytics           |
| AVRO        | Streaming and serialization      |
| XML         | Legacy systems, configuration    |
---

## Additional Notes

### What is Parsing?
Parsing is the process of analyzing a file or data structure to extract meaningful information. For example, when a program reads a JSON or XML file, it parses the content to understand its structure and retrieve the data.

### What is Columnar Storage?
Columnar storage organizes data by columns rather than rows. This format is highly efficient for analytical queries that focus on specific columns, as it allows reading only the required data, reducing I/O operations.

### What is Row Storage?
Row storage organizes data by rows, storing all the fields of a record together. This format is better suited for transactional workloads where entire records are frequently accessed or modified.