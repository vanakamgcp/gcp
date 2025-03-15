# Python Loops

# There are two loops in python 
#     while loop
#     for loop

# while loop

while <expression>:
    <statement>

cnt=0
while cnt>=0:
    print('given is greater than zero')
    print(cnt)
    cnt=-5

cnt=0
while cnt<=5:
    print(cnt)
    cnt=cnt+1

# we can use 'else' part in while loop also.
# when condition fails then loop exits and execute the part in else part.
cnt=0
while cnt<=3:
    print('This is iteration',cnt)
    cnt+=1
else:
    print('cnt exceeds three')


# minimalistic loop code ';' used to split statement.
cnt=1
while cnt==1:print('endless loop') ; cnt+=1


a = 5
while a > 0: a = a - 1; print(a)

# the above loop is same as below
while a>0:
    a=a-1
    print(a)


################ For Loop

It will only executes between the given range or sequence.
It wont stop until range or sequence completed.
If you want to exit or stop the loop, you can use control statements.

range(start_param,end_param)=> start to end-1

for i in range(1,4):
    print(i)
#1,2,3

for i in range(4):
    print(i)
#0,1,2,3

# it will throw error
for i in range('d'):
    print(i)

let = ['a','b','c','d']
#return the idx of list
for i in range(len(let)):
    print(i)

for i in let:
    print(i)
for i in range(-5,0):
    print(i)

for i in range(-5,1):
    print('*'*(-i))

for i in 'ajith':
    print(i)    #return all the letters in each line
else:
    print('outside of for loop')


# minimalistic control staement

op= [i for i in 'ajith']
op

# Loop control statements
    # Break, Continue, Pass
    Used to exit the loop, skip and iteration or ignore that condition.
    Loop control statements change execution from normal sequence.

 # Break
        It is used to terminate the loop when the condition satisfied.

    # For example you need to iterate the given string until 'k' or 'm' comes.]

    ip= 'ajithkumar'
    for i in ip:
        print(i)
        if i=='k' or i=='m':
            break

    # It will break the loop after found the letter 'k'

    #using while loop
    i=0
    while True:
        print(ip[i])
        if ip[i]=='k' or ip[i]=='m':
            break
        i += 1

    print("out of loop")

 # Continue 
    It is completely opposite to 'break' statement.
    It is used to skip the iteration not the loop.

For example we need to print values 1 to 10 except 6.

    ip= 'ajithkumar'
    for i in ip:
        if i=='k' or i=='m':
            continue
        print(i)
# for loop
for i in range(1,11):
    if i==6:
        break
    else:
        pass
    print(i)  #when i = 6 this line wont executed

# when the value is 6, it will continue to next iteration without print anything.

# we can do the same with pass also. what is the different
    
# pass
    It is used to do nothing.
    It is used for empty loops and empty functions.

for i in range(1,11):
    pass
    print(i)

def fun():
    pass

fun()

# no error will be raised
ip='ajith'

#nothing will happen in below loop.
for i in ip:
    if i == 'j':
        print('pass executed')
        pass
    print(i)


# # Difference between Pass and Continue :
# A pass statement signals to a loop that there is “no code to execute here.” 
# It’s a placeholder for future code. 
# A continue statement is used to force the loop to skip the remaining code and start the next iteration. 
