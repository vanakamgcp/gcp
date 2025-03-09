import pandas as pd


data = {'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'David', 'Bob'],
        'Age': [25, 30, 35, 25, 22, 30],
        'Score': [88, 75, 92, 88, 80, 75]}

df = pd.DataFrame(data)

df.drop_duplicates()

df