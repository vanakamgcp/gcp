Python Collections
    list[]
    tuple()
    set{}
    dict{key:val}

List :
    Mutable.
    Allow dups.
    Can Delete, Insert, update values into list.

List methods :
    insert(idx,value)
    extend(list|tuple|set)
    remove(val)
    pop(idx)
    del list[idx]
    clear()
    sort(reverse=True)
    copy()
    index(val)
    count(val)

x=['a','b','c']

1.x.insert(idx,value)

insert any values based on the idx.
it wont update any values. just insert only.

x.insert(3,'d') # 'd' is added at the end.

x   

x.insert(0,'A') # 'A' is inserted. all the values are moved to next idxs

x  #['A','a','b','c','d']

# below wont work
x.insert('d')
x.insert('a','d')


2. x.extend( list | tuple | set | dict)
    extend the list with another list or tuple or dict.

x=['a','b','c']
y=['x','y','z']
z=(1,2,3)
i={'i','j','k'}
j={'x':1,'y':2,'z':3}
x.extend(y)
x.extend(z)
x
x.extend(i)
x.extend(j)
x.extend('q')
x.extend('5')
x.extend(10)
when extend list with dict only keys are added to list. Not the values.
we can add single str at the end using extend. But we can not add int using extend.

3.x.remove(value)

x.remove('5')

x

x=[1,1,2,3,1,2] 
x.remove(1) #[1, 2, 3, 1, 2]
x
if we try to remove the value which is not in list then it will throw an ValueError.
if list has duplicate values then it will remove last last added value.

4.x.pop(idx)

remove the value by its idx.

It remove the value and returns it.

x = [1,2,3,4,5,6,2]
x.pop(2)
x.pop() # returns the removed value.

pop() without any idx removes the last added value.

x.pop(1) # returns value of idx:1 and removes it.

5.del x[idx]

delete the values by idx. if idx not given deletes the whole list.license

x=[1,1,2,3,4,5,6,7,8,9]

del x[] # invalid syntax

del x[0] # delets the idx 0

del x[0:5] # deletes the values from idx 0 to 4.

del x # deletes the list

6.x.clear()

clear the list.

x=[1,2,3,4,5,6,7]

x.clear() # [] empty list

7. x.sort()

alter the values based on the ascending order.

x=[2,7,8,5,3,1,4,6]

x.sort() # ascending order

x.sort(reverse=True) # descending order

y=['a','b','e','y','t','y','f']

y.sort()
y
y.sort(reverse=True)

8.x.reverse()

To reverse the values in list. It is not ascending or descending.

x=[8,8,9,6,4,7,2,1,3,5]

x.reverse()  #[5, 3, 1, 2, 7, 4, 6, 9, 8, 8]

9.x.copy()

x=[1,2,3,4,5]
y=[6,7,8,9]

y= x.copy() #list x is copied as y.

y
z=x # another way.

10. joining or merging two list.

x=['a','b','c']
y=[1,2,3]
z=['a','b','c']
i=[1,2,3]
j=[1,2,3]
i+j #[1,2,3,1,2,3]
i=x+y # ['a', 'b', 'c', 1, 2, 3]
j=x+x # ['a', 'b', 'c', 'a', 'b', 'c']
z=x+z # ['a', 'b', 'c', 'a', 'b', 'c']

# append y values to x
for i in y:
    x.append(i)

for i in x: 
    y.extend(i)

# by using extend we can not extend the int values. in that case we can use 'append'

11.x.index(value,[strt position])

# to return the idx of the given value.
# if the occurence is not given then first value of idx is returned.
x=[1,2,3,4,5,6,6]
x.index(5) #4
x.index(6) #5

# if the starting position is 2. then after idx 2 it will again start from 0

x=[1,2,3,6,4,5,6,6]
x.index(6) #3
x.index(6,2) #3
x.index(6,3) #3
x.index(6,6) #6
x.index(6,-1) #7
x.index(6,-4) #6
x.index(6,10) #6


12. x.count(value)
# return the number of occurence of give value in the list. 
# If the value is not in the list result will be zero.

x=[1,2,3,6,4,5,6,6]
x.count(6) #3
x.count(78) #0
x.count(a) #0


13.update list using idx,vaue

avengers = ['iron man','Thor','Hulk','spidy','cap']

#to print values
for i in avengers:
    print(i)

# to print idx
for i in range(0,len(avengers)):
    print(i)

for i in avengers:
    if i == 'iron man':
        avengers[avengers.index(i)]= 'RDJ'

avengers

dict in list

aji = {'name': 'ajith','roll':9566333985, 'package': '80 LPA'}
steve = {'name': 'steven','roll':953313114005, 'package': '110 LPA'}

name = [aji,steve]

filter(val,list)

the value will iterate over list and if val matches it will remove else it will return value.


list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# remove None from list1 and convert result into list
res = list(filter(None, li))
print(res)