# Datatypes
Variables are used to store the data which may be in int,str types.

Datatypes available in Python
Integer, Float, String, Complex, Boolean, 


1.Integers
    The numbers.
    There is no limit to how long an interger value can be. 
    The limit is constrained by the system memory we are using.

2. Float
    Numbers with decimal places.
    Range between (5.0*10e-324 to 1.8*10e308)
    Apart from those range result will become error 
example:
a = 10.0*10**309
a

3.String :
    Char and number mixed.
    No limit. we can save as long as system capacity.
4.Complex:
    Complex numbers.
    x+iy
5.Boolean.
    True, False


# Operators

There are lots of opertors available in Python.
1.Arithmetic Operators (+,-,*,/,//,%,**)
2.Assignment Operators (=,+=,-=,*=,/=,%=,//=,**=,>>=,<<=)
3.Comparison Operators (==,!=,>,<,>=,<=)
4.Logical Operators (and,or,not)
5.Identity Operators (is,is not)
6.Membership Operators (in,not in)
7.Bitwise Operators (not covered)

#####################################################################
#Arithmetic Operators
#####################################################################

print(1+1) #2
print(-2+1) #-1
print(+1+4) #5
print(1+1.2) #2.2
print(1+1.0) #2.0

# Whenever we add a float to integer the output becomes in float format even when output is whole number.
# Also the datatype is changed from integer to float.

type((1+1.0))  #float

# When using '+' operator to strings then it will act as a concatination operator.
# It doesn't matter how much strings we give it will concatinate all the given strings.

print('a'+'b')  #ab
print('a'+'ab') #aab
print('a'+'b'+'c') #abc
# when we use '+' operator to string and integer or float compination it will throw an TypeError.
print (1+'a')  #TypeError : unsupported operand types

#'+' works as addition operator when works with int and float. For strings it works as concat operator.

int+int
float+float
int+float
str+str
###########################################

print(1-1)  #0
print(-1-1) #-2
print(0-0) #0
print(-0-0) #0
print(-1.3-1) #-2.3
print('a'-'ab') #TypeError : unsupported operand type(s) for -
print('a'-1)  #TypeError : unsupported operand type(s) for -
# We can not do anything on string using '-' operotor like we do for '+' operator to concatinate.

# '-' operator is only for string and float.

int+int
float+float
int+float

################################################

print(2*2) #4
print(-2*2) #-4
print(1.2*2.3) #2.76
print(9.3333333333333+0.7) #10.0333333333333
print(0*0) #0
print('a'*'a') #TypeError : can't multiply sequence by non-int of type 'str'

# We can not use '*' against str vs str.

print('a'*2) #aa
print('abc'*3) #abcabcabc (3 times abc is repeated)
print('a'*-3) #  (no output.just empty. But output type is str)
len('a'*-3)  #0  (So nothing will be displayed)
type('a'*-3) #str
type('a'*3) #str
print(3*'a') #aaa
# If we use '*' against str and int, it will add the strings against given integer.
print('a'*1.0) #TypeError

int+int
float+float
int+float
str+int

#######################################################
# Division
# '/' always returns a float type. Even it is whole number.
# Supports only int and float.

print(12/2) #6.0
print(12.0/2.0) #6.0
print('aa'/'a') #TypeError
print('aa'/1) #TypeError
int+int
float+float
int+float
#######################################################
#Floor Division
# '//' always rounds(truncates) the division
# Supports only int and float.

print(5/3)   #1.6666666666666667
print(5//3)  #1
print(20/7)  #2.857142857142857
print(20//7) #2
int+int
float+float
int+float
########################################################
# '%' Modulus operator returns the reminder
# Supports only int and float.
print(10%3) #1
print(10%3.0) #1.0
print('aa'%1) #TypeError
print('aa'%'a') #TypeError

int+int
float+float
int+float

#########################################################
# '**' Exponentiation operator

print(2**4) #16
#2*2*2*2  two is multiplied by four times.

print(2**2.0) #4.0
print(2.0**2) #4.0
print('a'**2) #TypeError

# works only with int and float
