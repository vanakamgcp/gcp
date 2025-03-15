Set:
- unordered
- unindexed
- Dups are not allowed
- Access via loop only. because of no index.

s = {'rdj','thor','banner','cap'}

s

Set methods:
- add(val)
- clear()
- copy()


1.s.add(val)
    - adding value 

s.add('ajith')

s

# it wont allow duplicates also wont raise any error.
s.add('ajith') 

s

2. s.clear()
    - clear the list
    - no params
    
s = {'rdj','thor','banner','cap'}

s.clear()

2. s.update(set | list)
    - merge set with another set or list.
    - exclude dubs.

s1={'hawkey','black widow'}

s.update(s1) # s1 values are added to s.

s

li = ['spidey','ant man']

s.update(li)

s

3. s.copy()
    - returns the copy of set

s = {'rdj','thor','banner','cap'}

s1= s.copy()

s1

    - it is same as 
    s2 = s

s2

4. s1.difference(s2)
    - display s1 values which are not present in s2.

s1= {'aji','abi','moni'}

s2 = {'aji','abi','moni','san'}

s1.difference(s2)   # nothing

s2.difference(s1)   # 'san'

s1 = {'jayakumar','thangam','aji','abi','moni'}

li= ('aji','abi','moni')

s1.difference(li)   # {'jayakumar', 'thangam'}

5. s1.difference_update(set|list)
    - it will update s1 by removing values which are present in s2.

s1= {'aji','abi','moni'}

s2 = {'aji','abi','moni','san'}

s2.difference(s1)   # 'san'

s2.difference_update(s1)

s2  #'san'

5. s.discard()
    - remove the specified item by its value

s = {'rdj','thor','banner','cap'}

s.discard('aji')    #no error

s.discard('cap')    # removes 'cap' value

s

6. s1.intersection(s2|l2)
    - displays common values between s1 and s2|l2

s1= {'aji','abi','moni'}
s2={'aji','rdj','thor'}
l2=['aji','rdj','thor']

s1.intersection(s2) # {'aji'}
s1.intersection(l2) # {'aji'}

7. s1.intersection_update(s2|l2)

s1= {'aji','abi','moni'}
s2={'aji','rdj','thor'}
l2=['aji','rdj','thor']

s1.intersection_update(s2) 
s1 # {'aji'}
s1.intersection_update(l2) 
s1 # {'aji'}

8. s1.isdisjoint(s2)
    - returns whether two sets have intersection or not.
    - returns 'true' if s1,s2 contains common values.
    - returns 'false' if s1,s2 contains no common values.

s1= {'aji','abi','moni'}
s2={'aji','rdj','thor'}
l2=['aji','rdj','thor']

s1.isdisjoint(s2) # false
s1.isdisjoint(l2) # false


s1= {'abi','moni'}
s2={'aji','rdj','thor'}
l2=['aji','rdj','thor']

s1.isdisjoint(s2) # true
s1.isdisjoint(l2) # true

9. s1.issubset(s2|l2)
    - 'true' if all s1 items present in s2. (s2 is subset of s1)
    - 'false' if not all s1 items present in s2.

s1= {'aji','abi','moni'}
s2={'aji','rdj','thor'}
l2=['aji','rdj','thor']

s1.issubset(s2) # False
s1.issubset(l2) # False

s1= {'aji','abi','moni'}
s2={'aji','abi','moni','rdj','thor'}
l2=['aji','abi','moni','rdj','thor']

s1.issubset(s2) # True
s1.issubset(l2) # True

10. s1.issuperset(s2|l2)
    - it is complete opp to issubset().
    - 'true' if all s2 items present in s1. (s2 is superset of s1)
    - 'false' if all s2 items not present in s1.

s1= {'aji','abi','moni'}
s2={'aji','rdj','thor'}
l2=['aji','rdj','thor']

s1.issuperset(s2) # False
s1.issuperset(l2) # False

s1= {'aji','abi','moni','rdj','thor'}
s2={'aji','rdj','thor'}
l2=['aji','rdj','thor']

s1.issuperset(s2) # True
s1.issuperset(l2) # True

11. s1.pop()
    - removes random values from the set.
    - no arguements.

s1= {'aji','abi','moni','rdj','thor'}

s1.pop() # 'rdj'

s1 # {'thor', 'moni', 'aji', 'abi'}

3. s.remove(val)

s.remove('ajith') # ajith is removed from set

s.remove('ajith') # it will throw key error bcz value ajth is not present.

4. s.discard(val)
- if value is not present it wont raise any error.

s.discard('ajith')

5. s.pop()
    - deletes the last item.
    - since set is unordered. any item can be removed.


6. s.copy()

s2= s.copy() # copies s into s2

7. s.union(s|l) 
        - it wont update set 's' with another set or list.
        - it will just display the common unique records from  s and s1.


s2 = {'badman','superman','flash'}

s.union(s2)

s

8. s.update(s|l)
    - it will update s with another set. exclude dublicates.
    
    s.update(s2)

    s
9. s.difference(s1)
    - (s1-s2)
    - display s1 values which are not present in s2.

s1 = {'a','b','c'}
s2 = {1,2,3}

s1.difference(s2) # {'b', 'a', 'c'}

s1 = {'a','b','c'}
s2 = {1,2,3,'a'}

s1.difference(s2) # {'b', 'c'}

10. s1.difference_update(s1)
    - update s1 values by removing values which are present in s2.

s1 = {'a','b','c'}
s2 = {1,2,3,'a'}

s1.difference_update(s2) 

s1 # {'b', 'c'}

s1= {1,2,3}

s2={'a','b','c'}

s1.difference_update(s2)

s1  # {1, 2, 3}

s1= {1,2,3,'c'}

s2={'a','b','c'}

s1.difference_update(s2)

s1  # {1, 2, 3}

s1.update(s2)

s1 #{'b', 1, 2, 3, 'a', 'c'}

