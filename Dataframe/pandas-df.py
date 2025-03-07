import pandas as pd

# Create a DataFrame from a csv file
df = pd.read_csv('/Users/ajithkumarj/coder_mode/gcp/sample_data/employees.csv')

# RETRIVE THE DATA (SELECT)

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

# FILTER THE DATA (WHERE)

# Filter the data based on a condition
df[df['SALARY'] > 8000]

df[df['FIRST_NAME'] == 'Steven']

# Filter the data based on multiple conditions
# AND Operator (&)
# Each conditions should be enclosed in brackets otherwise it will throw an error.
df[(df['DEPARTMENT_ID'] == 50) & (df['SALARY'] > 8000)]

df[(df['HIRE_DATE'] < '2005-01-01') & (df['SALARY'] < 8000)]

# OR Operator (|)
df[(df['DEPARTMENT_ID'] == 40) | (df['SALARY'] > 8000)]

df[((df['DEPARTMENT_ID'] == 50) & (df['SALARY'] > 8000)) | (df['DEPARTMENT_ID'] == 90)]

# IN, NOT IN

# df[(df['col_nm'].isin([cond]))]

df[((df['DEPARTMENT_ID'].isin([40,30])) & (df['SALARY'] < 8000))]

# NOT IN

# "~"(tild) condition to apply NOT condition
df[~df['DEPARTMENT_ID'].isin([10,20,30])]

df[df['SALARY'] == 8000]

df[~(df['SALARY'] <= 8000)][['FIRST_NAME','SALARY']]

df[~(df['SALARY'] < 18000)]

# BETWEEN
# df[df['col_nm'].between('start_int','end_int',inclusive='neither','left','right','both')]
# By default it includes both values. We can ignore values with "inclusive" keyword.
df[df['EMPLOYEE_ID'].between(100,111)]

df[df['HIRE_DATE'].between('01-01-2004','31-12-2005')][['DEPARTMENT_ID','HIRE_DATE']]

df[df['DEPARTMENT_ID'] == 30][['DEPARTMENT_ID', 'SALARY']]

#LIKE and NOT LIKE relevant
# First we need to convert filter column to str or int to apply the filter condition.
# Usual string and int methods can applied to columns.

df[df['FIRST_NAME'].str.contains('St',case=False,na=False)]

df[df['FIRST_NAME'].str.startswith('A')]

df[~df['FIRST_NAME'].str.contains('St',case=False,na=False)]

df[~df['FIRST_NAME'].str.startswith('A')]
