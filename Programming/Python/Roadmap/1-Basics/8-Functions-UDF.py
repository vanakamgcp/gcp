# Functions
# Reusable block of code for certain usage.

def func_name():
    # functionality of function


# Sample function
def myfunc():
    print("Hello, Ajith !!")

myfunc()

# without any arguement we can write function for some particular repeated task.
# for example whenever call the function it should return the list of file in particular path.

# arguments 
# we can add many arguments as we want.
# the term parameter or argument both are indicated for the same thing. Both are to pass the information to the function.

def my_fun(nm):
    print("Hello,",nm," !!!")

my_fun('ajith') # Hello, ajith !!!
my_fun(123)  # Hello,123 !!!

# write a function to concate fname and lname
def full_nm(fnm,lnm):
    print("Your full name is,",fnm,lnm)

full_nm('ajithkumar','jayakumar')

# passing arguments with defined datatype

def full_nm(fn,ln):
    print(fn+' '+ln)

full_nm('ajith','kumar')

full_nm('ajith')

# if we miss any arguement in function then it will throw an typeerror 
# missing one required positional arguement

# setting default value for arguements
# arg= default value

def full_nm(fn,ln='no last name'):
    print(fn+' '+ln)

full_nm(('ajith'))
full_nm('ajith','kumar')

def full_nm(fn,ln=''): #without any value
    print(fn,ln)

full_nm('ajith')

# arbitrary arguements (*args)

# If we dont know how many arguments will pass to the function, then we can use arbitrary arguements.
# just putting '*' symbol before arguement.

# Then the given arguements are passing to function like tuple.

def sum_fn(*args):
    sm=0
    for i in range(0,len(args)):
        sm=sm+args[i]
    print(sm)

sum_fn(1,2,3,4,5)

# return only leap years of given year range

def leap_yr(*args):
    yr=[]
    for i in args[::]:
        if i%4==0:
            yr.append(i)
    print(yr)

# creating list for storing years from 2000 to 2022
yr=[]
for i in range(2000,2023):
    yr.append(i)

# it is throwing error.
# reason is the input for *args are taken as tuple. 
# we our input is list then we need to convert it into tuple in function otherwise it will throw an error.
leap_yr(yr)

#if we manually enters the values it is working. But list did not work.
leap_yr(2000,2001,2003,2004,2006,2008,2012)

# creating the same function with list to tuple.
def leap_yr(*args):
    if type(args) == "<class 'list'>":
        args=tuple(args)
    else:
        yr=[]
        for i in args[::]:
            if i%4==0:
                yr.append(i)
    print(yr)

yr=[]
for i in range(2000,2023):
    yr.append(i)

leap_yr(yr)

li=['a','j','i']
ty=type(li)
print(ty)

tu=tuple(li)
tu


li = [1, 2, 3, 4]
li[1:3] = [5, 6, 7]
print(li)