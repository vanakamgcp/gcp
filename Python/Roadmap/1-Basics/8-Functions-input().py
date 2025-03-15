input()
It accept input from the user.

syntax: input(["input mesaage to display"])

x = input() 

the user provided value is assigned to 'x'.

name =input("Enter your name : ")

whatever values we give it only taken as string.

If we need to take input as str,int,float. we can convert str to required datatype.

name = input("Enter your name : ") #ajith
rollno = input("Enter your rollno : ") # 1234
avgmark = input("Enter your avg marks : ") # 80.5

type(name)  #str
type(rollno) #str
type(avgmark) #str

Here all the inputs from user are stored as string.

To get all the inputs as required datatype.

name = input("Enter your name : ") #ajith
rollno = int(input("Enter your rollno : ")) # 1234
avgmark = float(input("Enter your avg marks : ")) # 80.5

type(name)  #str
type(rollno) #int
type(avgmark) #float

To get multiple inputs in single input()

name,rollno,avgmark = input("Enter your name,roll number, avg mark seperated by space :").split()

type(name)  #str
type(rollno) #str
type(avgmark) #str

To get multiline input,
After first line if we type enter it will stops the execution to avoid this we can follow the following approach.
data = []
print("Tell me about yourself")
while True:
    line = input()
    if line:
        data.append(line)
    else:
        break
finalText = '\n'.join(data)
print("\n")
print("Final text input")
print(finalText)

pass input arguements to python file while running in CLI(commend line interface).

sys module is used to get values for file program.

sys.argv - get arguements from CLI

argv is list structure.

it takes file name as the first arguement, then takes the given argument.
So if we pass three arguements the length will be four. 
Because it included file name.



