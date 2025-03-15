# Exercise 1: Print First 10 natural numbers using while loop

i = 1

while i<=10:
    print(i)
    i+=1    

# Exercise 2: Print the following pattern
""""
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
"""
n=5
for i in range(1,n+1):
    for j in range(1,i):
        print(j,end=' ')
    print("")   # for next line 

# another way to do with adding one extra variable
n=5
j=''
for i in range(1,n+1):
    j= str(j)+str(i)
    print(j)

# ex : 3 Calculate the sum of all numbers from 1 to a given number

n = 10
m=0
for i in range(1,n+1):
    m=m+i
print(m)

# another way
n=10
m=sum(range(1,n+1))
m

# Exercise 4: Write a program to print multiplication table of a given number
n=2
for i in range(1,11):
    print(i*n)


# Exercise 5: Display numbers from a list using loop
# Write a program to display only those numbers from a list that satisfy the following conditions

# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop

#  Given: 
numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i%5 == 0:
        if i>150:
            continue
        elif i >500:
            break
        else:
            print(i)
    else:
        pass

for i in numbers:
    if i>150:
        continue
    elif i>500:
        break
    elif i%5==0:
        print(i)
    else:
        pass


for i in numbers:
    if i>500:
        break
    elif i>150:
        continue
    elif i%5==0:
        print(i)
    else:
        pass