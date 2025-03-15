Pandas Features :

Fast and efficient dataframe obj with default and customized indexing.
Can handle variety of file formats.
Columns from datastructure can be deleted or inserted.
Group by data for aggregation and transformations. 
High performance merging and joining of data.
Time series functionality.

To install pandas library

"pip install pandas"

There are three datastructures in pandas,
        Series    - 1D - Like list
        Dataframe - 2D - rows and columns
        Panel     - 3D - 

# Series Object : ######################################################################

pd.Series(data,index=idx)

Series contains the sequence of values and explicit sequence of indices.
(i.e. values and index)
Default index values are integers.
Index values are ordered whether it is integers or user given indexes.


import pandas as pd

data = pd.Series([1,2,3])  # datatype : int64

data

type(data)

# If we add one float64 values into series of int64 values.
# Then all the values changed into float64 values.

data = pd.Series([1,2,3,4.0])

data

data.values # array([1., 2., 3., 4.])
data.index  # RangeIndex(start=0, stop=4, step=1)

# values and index can be accessed to loops.

for i in data.values:
        print(i)

for i in data.index:
        print(i)

# values can be accessed from index
# the value returned is also series type not list.

data[0] # 1.0

data[:2]

####################################
# changing index values from integers to alphabets ----------------------------------

data = pd.Series([1,2,3,4],index=['a','b','c','d'])

data

data['b']

data = pd.Series([1,2,3,4],index=['a','b','c']) 
# ValueError: Length of values (4) does not match length of index (3)

# length of values should match the length of index

data = pd.Series([1,2,3,4],index=['a','b','c','d','e'])

data = pd.Series(10)

data

# Note : 
data= pd.Series(10, index=[2,4,5])

data

# If we provide single value for series of index. That single value assigned to all the index.


#######################################

# Create series from dictionary --------------------------------------

# All the dict keys become series's indices.

dept_strnth = {'mech':67, 'cse':60, 'ece':51, 'civil':30}

data = pd.Series(dept_strnth)

data

data['mech']
# access values from 'mech' to 'ece'
data['mech':'ece']

data['ece':'mech']  # Series([], dtype: int64)

data= pd.Series({1:'a', 2:'b',3:'e'})

data

If we assign explicit index for dictionaries.
Then dict keys become invalid. And explicit index are taken for index.

data= pd.Series({1:'a', 2:'b',3:'e'}, index=[1,2])
# value 'e' is ignored. Because we gave only 2 index for 3 values.
data

# Dataframe: ####################################################################

Series is one dimentional array with flexible row indices, 
Dataframe is a analog of two dimentional array with both flexible row indices and flexible column names.
(i.e)Storing data in tabular format in python.

# data frame takes dict keys as columns.
# if dict doesnt have any common keys, It combines it and add values as 'NaN' for not available keys.

tamil_marks = {'ajith': 85, 'abi': 90, 'moni':100}
english_marks = {'ajith': 80, 'abi': 75, 'moni':96, 'san':98}

tamil = pd.Series(tamil_marks)
english= pd.Series(english_marks)


# Now we are adding colum names as 'eng_marks' and 'tam_marks' to this Series.

marks = pd.DataFrame({'eng_marks':english_marks,'tam_marks':tamil_marks})

marks

# access df index and columns
marks.index
marks.columns

# accessing dataframe via colm name
marks['tam_marks']

# if both dictionaries doesn't have any common keys

sci_marks = {'aji':95,'abi':80, 'moni':90}
soc_marks = {'raj': 80, 'ana': 90, 'san': 95}

marks = pd.DataFrame({'sci':sci_marks,'soc':soc_marks})

marks

# create dataframe from single series obj

sci_marks = {'aji':95,'abi':80, 'moni':90}
science = pd.Series(sci_marks)

sci = pd.DataFrame(science,columns=['sci_marks'])
sci

# Daframe from list of dict

data = [{'a':i,'b':2*i} for i in range(3)]

data

dict_df = pd.DataFrame(data)

dict_df