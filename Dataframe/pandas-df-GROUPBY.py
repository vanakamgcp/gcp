import pandas as pd

# Create a DataFrame from a csv file
df = pd.read_csv('/Users/ajithkumarj/coder_mode/gcp/sample_data/employees.csv')

df.groupby('DEPARTMENT_ID')['SALARY'].sum()

df.groupby('DEPARTMENT_ID')['SALARY'].max()
