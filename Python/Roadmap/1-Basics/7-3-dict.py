d['key']
d.get('key'[,replacement value])

d.keys()
d.values()
d.items()

d['key'] = val
d.setdefault('key',val) # if key is not there the item is added else it skip the process

d.pop(key)
d.popitem()
del d[key]
d.clear()

d3= {**d1,**d2}

d1.update(d2)

# ------------------------------------------------

person = {'name': 'aji','name': 'steve'}

person # if keys are same then last key value item only present in dict

person = {
    'name': 'ajith',
    'oor': 'india',
    'love': 'yes',
    'dept': 'IT',
    'age': 28
}

# Get keys,Values --------------------------------------------------------------

# to get value by keys
person['name']

person['name','oor'] # KeyError: ('name', 'oor')

# if key doesnt exist it will throw an error.
person['dob'] #KeyError: 'dob'

d.get('key',[replacement value for non available key]) # get value by key

person.get('name')

# it wont throw error if key is not present. it simply return None.
person.get('dob')

person.get('dob',"90's kid") # dob is not present so it return 90's kid

for i in person:
    print(i)

# to return only keys.
for i in person.keys():
    print(i)

# check wheather key is in dict or not
'oor' in person.keys() # True
'nat' in person.keys() # False
'job' in person # False # also can vomit .keys()

# to return only values.
for i in person.values():
    print(i)

# check values in values.
'ajith' in person.values() # True
'Indian' in person.values() # False
28 in person.values() # True

# to return key and value pairs.
for i in person.items():
    print(i)

for key,val in person.items():
    print(key,val)

# adding items to dict ----------------------------------------------------------

person['dob'] = 1990
person['name'] = 'steve' # the name is changed from 'ajith' to 'steve'

person 

if 'nat' not in person.keys():
    person['nat']='Indian'

# same like above
# if lan1 is not present it will added to dict. if present it skip the adding
person.setdefault('lan1','Tamil')
# name is already there so it will skip the operation
person.setdefault('name','aji')

# Removing Items : ---------------------------------------------------------
d.pop('key')

# remove and return the removed value based on the given key.
person.pop('lan1')

person

# remove last item in the dict

d.popitem()

person.popitem()

# delete by giving key value

del d['key']

del person['dob']

person

# delete all the items 

d.clear()

person.clear()

person # empty list

# Merge two dict ------------------------------------------------------------------

dict1 = {'x':1,'y':2,'z':3}
dict2 = {'a':4,'b':5,'c':6, 'x':1,'x'=4}

dict3 = {**dict1 , **dict2}

dict3 # x items in dict2 are omitted.

# update dict values with another dict

person1 = {'name':'ajith','qual': 'BE','exp' : 4}
person2 = {'name':'aji','qual': 'BE-MECH','exp' : 6, 'loc' : 'CHE'}

person1.update(person2)

person1 # existing values are updated and new values are added