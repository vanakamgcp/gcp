CREATE OR REPLACE TABLE bigquery-tutorial-445512.temp.temperature_data (
  id INT64,
  recordate DATE,
  temp FLOAT64
);

INSERT INTO bigquery-tutorial-445512.temp.temperature_data (id, recordate, temp)
VALUES 
  (1, DATE '2024-01-01', 30.0),
  (2, DATE '2024-01-02', 35.0),
  (3, DATE '2024-01-03', 33.0),
  (4, DATE '2024-01-04', 36.5),
  (5, DATE '2024-01-05', 36.0),
  (6, DATE '2024-01-06', 37.2),
  (7, DATE '2024-01-07', 34.0),
  (8, DATE '2024-01-08', 38.0);

drop table bigquery-tutorial-445512.temp.temperature_data;

-- 1. return the data if the temp is greater than previous day's temp