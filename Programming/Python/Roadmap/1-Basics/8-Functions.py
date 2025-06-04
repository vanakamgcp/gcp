'''
Functions :
Reusable block of code for repeated usage.
    
Types:
    BuiltIn functions - range(),sum(),type(), id()..etc
    User Defined Functions - User created functions for specific usage.

Syntax :

    def func_name(params):
        <<<function body>>>
        return output

    def - define function
    params - value passing to the function. funcation can be created without params too.
    return - the output of function it is optional. 
    Because some function used to do the operation not neccessary to return anything.
'''
# Creating functions withour params : -----------------------------------------------------------

def name():
    print ('what is your name ?')

# Calling function :
name() # what is your name ?

# Creating function with params : ----------------------------------------------------------------

# here passing two params and do sum operation
def sum(x,y):
    print(x+y)

sum(10,5) #15

sum('ajith','kumar') # ajithkumar

# Creating function using params with return values : -----------------------------------------------

def calc(a,b):
    add = a+b
    return add

calc(5,6) # 11

'''
The return keyword stops the execution of function. it wont continue further
'''

def calc(a,b):
    add = a+b
    return add
    print('Addition is completed')

# it wont print the 'print statement' in function
calc(1,5) # 6 

def calc(a,b):
    add = a+b
    print( add)
    print('Addition is completed')

calc(1,5) # 6 Addition is completed

# if empty 'return' is used then it will return nothing.
def calc():
    return

# return multiple values

def calc(a,b) :
    add=a+b
    sub=a-b
    multi=a*b
    div=a/b
    return add,sub,multi,div

calc(10,5) # return result as tuple

a,b,c,d = calc(15,5)
a

# Using imported functions from module -------------------------------------------------------
# randint from random module generates random int between 
from random import randint

randint(0,50) # give random int between given number

# DocString ----------------------------------------------------------------------------------

# Docstrings are document string added to the code to explain about the to others.
''' This is Docstring '''
# The docstring are enclosed by ''' or """
def sum(a,b):
    ''' This function takes two args and returns sum of it '''
    return a+b

# to get docstring of function, we can use '__doc__' attribute
sum.__doc__
# also we can use help() function to get docstring
help(sum)

# example multiline docstring

def sum(a,b):
    ''' This function is used to sums the given two numbers.

        It take only two args.

        It uses return statement to return the result
    '''
    return a+b

sum.__doc__

# The Pass statement ------------------------------------------------------------------------------
# pass keyword is used to do nothing. 
# In some situation we need to create function to do nothing. 
# That time we can use 'pass'.

def addition(a,b):
    ''' THis is do nothing'''
    pass

addition(10,15)

# Variables in functions. ----------------------------------------------------------------------------
# Local and Global variables in functions.

# Local Variables :
# Variables which are used inside function and which can not be accessed outside of function.

def addition(a,b):
    add_loc = a+b # local variable
    return add_loc

# here add_loc variable is can not accessed outside of the function.

# global variable :
# It can accessed and manipulated by many funcions.
# It is assigned outside of code.
# The value of global variable remain unchange untill the value is changed globally.
# To change global variable in function, use 'global' keyword while using variable inside function.

gvar = 10

def summa():
    gvar = 5 # this is local variable copy of glabal variable.
    return gvar

summa() # 5

gvar # 10 # Here the value is remain same

def summa1():
    return gvar

summa1() # 10

# to change value of global variable in function, have to use global keyword.

gvar = 10

def summa():
    global gvar # mentioning to gvar as global variable 
    gvar = 15
    return gvar

summa() # 15

gvar # 15

# nonlocal variable --------------------------------------------------
# nonlocal variables act as global variable for nested functions.
# 'nonlocal' keyword is used to declare this variable.

def outer_func():
    x,y=100,100
    def inner_func():
        # declare local variable as nonlocal to act as global variable.
        nonlocal x
        x=50
        y=50 # here y is local variable only
        print("value of x,y in inner function",x,y)
    inner_func()
    print("value of x,y in outer function",x,y)

outer_func()

# Python Arguements
# Arguements is value,variable or object passing to function.

# Positional Arguments :
# Passing args in positional order.

def sub(a,b):
    sub = a-b
    return sub

sub(10,5) # a=10,b=5

sub(15,20) # a=15,b=20

sub(10,5,15) # TypeError: sub() takes 2 positional arguments but 3 were given

# Keyword arguements
# when passing values we use args name.

sub(a=10,b=15)

sub(b=20,a=5)

# default arguements
# If default values are assigned while defining function. 
# then when calling function we dont need to provide that arguements.

def msg(name='guest'):
    print('Welcome ,{} !!!'.format(name))

msg('ajith') # Welcome ,ajith !!!

msg() # Welcome ,guest !!!

# Vary length or Arbitary args
# We can give many args.
# all those args are passed into function as 'tuple'
# '*' is used to mention vary args

# total marks function
def total(*subs):
    sum = 0
    for i in subs:
        sum+=i
    return sum

# passing five values
total(80,92,80,95,90) #437

# passing three values
total(80,75,98) #253

# Keyword args --------------------------------------------------------------

# used when we do not know about number of args gonna passing.
# the values are passed as key value pair and as a dictionary format.
# '**' is mention kwargs

def person_details(**details):
    for key,values in details.items():
        print (key,' ',values)


person_details(name='ajith',location='chennai',qualification='BE')

person_details(name='Steve',location='Silicon Valley',qualification='Drop out',experience = 6)

# Recursive Functions ---------------------------------------------------------------------------
# Recursive functions are the functions it calls itself again and again
# Uses :
# By using recursive, we can reduce the length of the code.
# The readability of code improves due to code reduction.
# Useful for solving a complex problem


# example
def factorial(x):
    if x==1:
        return x
    else:
        return x * factorial(x-1)
    
factorial(5)
factorial(1)

# this works in this way

factorial(5)
    
# 5*factorial(4)
# 5*4*factorial(3)
# 5*4*3*factorial(2)
# 5*4*3*2*factorial(1)
# 5*4*3*2*1 = 120

# Anonymous Function or Lambda Functions -----------------------------------------
# Function withour name is called Lambda functions
# This is for instant use also for one time usage

# while creating instead of 'def' keyword we use 'lambda'
'''
Syntax :
lambda arg_list: expression
'''

# function without lambda

def sum(a,b):
    return a+b

sum(10,5)

# with lamba function

x = lambda a,b : a+b
x(10,5)

# if,else in lambda

result = lambda x: "{} is even".format(x) if x%2==0 else "{} is odd".format(x)
result(5)

# check which is greater and smaller in given numbers
result = lambda x,y: 'x is smaller' \ 
    if x<y else ('x is greater' if x>y \
                 else 'x is equal to y')

# '\' is used to split the line
result(10,10)

# filter(),map(),reduce()
# filter()

# filter(function,args)

x=list(filter(lambda x : x += x,[-10,5,-1,9,-15]))
x
x=list(map(lambda x : x > 0,[-10,5,-1,9,-15]))
x
from functools import reduce
list1=[-10,5,-1,9,-15]
add = reduce(lambda x : x > 0, 10)
add

x=max(([-10,5,-1,9,-15].remove(9)))

print([1,2,3].remove(1))