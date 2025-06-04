# conditionals

there are three conditionals in python
    if
    else
    elif
    match case

# if conditional will run if given statement is true or satisfied.
    if <condition>:
        <statement>
    
if True:
    print('ajith')

if true:            # Python is case sensitive so 'true' is not boolean
    print('ajith')

if 1:
    print('ajith')

if 0:
    print('ajith')

if 3:
    print('ajith')

if -1:
    print('ajith')
# As per python '0' is 'False' and '1' is 'True'

x=1
y=5

if x<y:
    print('x is less than y')

# else statement
# Whenever the if condition fails then automatically python execute the statement in else part.

    if <condition>:
        <statement>
    else:
        <statement>


if x>y :
    print('x is greater than y')
else:
    print('x is less than y')

if 1:
    print('1 is considered as true')
else:
    print('0 is considered as false')

# '0' ku mattum than fail aaguthu. Matha ella numbers kum fail aagala


# elif statement
# This is used to apply multiple conditions
# If everything fails then execute the statement from 'else' statement

    if <condition>:
        <statement>
    elif <condition>:
        <statement>
    .
    .
    else:
        <statement>


x=10
y=10

if x>y:
    print('x is bigger')
elif y>x:
    print('y is bigger')
else:
    print('both are same')


# use minimal code for 'if..else' statement
variable = <'statement for if'> if <condition> else <'statement for else'>

x,y=10,15

z='x is bigger' if x>y else 'y is bigger'
print(z)

# Nested conditions
sub='Math'
mark=40

if sub=='Math':
    if mark>=45:
        print('pass')
    else:
        print('pass mark is above 45')
else:
    print('enter maths mark only')


# MATCH CASE statement
# It is powerfull and simple

nm='ajith'

match nm:
    case 'ajith':
        print('hello ajith')
    case 'vijay':
        print('hello vijay')
    case other:
        print('Nee yaarune theriyathu podaaaa')


for i in range(2,5):
    print(i)

def is_leap(year):
    leap= False
    if (year%4)==0:
        if (year%400)==0:
            leap=True
        elif (year%100)==0: 
            leap=False
        else:
            leap= True
    else:
        leap=False
    return leap

year = is_leap(1992)
print(year)

1992%400
