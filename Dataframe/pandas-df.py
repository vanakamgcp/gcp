import pandas as pd

# Create a DataFrame from a csv file
df = pd.read_csv('/Users/ajithkumarj/coder_mode/gcp/sample_data/employees.csv')

# SELECT 

# retrive column names
# It returns Object datatype which is a pandas Index object.
df.columns

# Store column names in a list
columns = df.columns.tolist()

# Select data from all the columns
df

# Select a specific columns
df['FIRST_NAME']

# Select multiple columns
df[['FIRST_NAME', 'LAST_NAME']]

# df.loc[row_selection, column_selection]
df.loc[:, ['FIRST_NAME', 'LAST_NAME']]

# SELECT first 2 columns
df.iloc[:, [0,1]]

# select first three columns
df.iloc[:, 0:3]

# For fixed column positions, we can use iloc method to select the columns.