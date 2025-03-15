Tuple:
    Same as list.
    But inmutable so faster than list also take less memory than list.
    Can not insert, delete, update the elements in list.
    Allow duplicates.
    Only for accessing values.

Note: If we need to perform any operation like insert, update, delete in tuple. 
        Then convert tuple to list, make operations , convert back to tuple.


Methods :
    count()
    index()

x=(1,2,3,4,5,1,1,2,2,1,2)
type(x) #tuple

1.x.count(val)

x.count(1) #3

2.x.index(val,[starting postion])

x.index(1,4)
# packing is nothing but assigning values to tuple.

# Unpacking in tuple.
# Unpacking is assigning the tuple values directly to variables.

tu = ('aji','abi','moni')

# Unpacking 'tu' values to variables first,second,third
(first,second,third)= tu

first #aji
second #abi
third #moni

# assigning multiple values to single variable in unpacking
# * symbol is used to do that.
# tuple values should match with the unpacking variables.
(first,*other) = tu

first #aji

other # ['abi','moni']

avengers = ('cap','iron man','thor','hulk','hawkey','black widow')

(old,*strongest,normi1,normi2) = avengers

old # cap
strongest #['iron man', 'thor', 'hulk']
normi1 #hawkey
normi2 #'black widow'

Join in tuple.

t1=(1,2,3)
t2=('a','b','c')

t1+t2 #(1, 2, 3, 'a', 'b', 'c')

t1*2 #(1, 2, 3, 1, 2, 3)

t2*2 #('a', 'b', 'c', 'a', 'b', 'c')
