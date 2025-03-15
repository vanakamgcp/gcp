
Variable:
    It holds the data.
    Pointer to the memory location where data is stored.
    Memory is created first and data is stored in that memory next. 
    finally variable is assigned as pointer to that location.

    n=300

    Here, Memory location is created first and '300' is stored in that location.
    finally, 'n' is assigned as pointer to that location.

    To see the memory location id() method is used.
    check the datatype of data type() method is used.

    n=300
    print(id(n))  # 2028588670832
    print(type(n)) # <class 'int'>

    if we assign same variable to another variable, memory loc will be same but pointer is diff.

    a = 10 #here 10 is assigned to a
    a = b # assign a to b

    Now memory location of a and b is same.
    id(a) #2028587647184
    id(b) #2028587647184

if we externally (not like a=b) assign values between (-5,256) to variables. the memory location will be same.

    a = 10 
    b= 10  # externally assigns 10 to b. not like a=b
    id(a) #2028587647504
    id(b) #2028587647504
    But memory location will be same. and it will same for values between (-5,256)

if values exceeds (-5,256),
    a = 300
    b = 300
    id(a) #2028588670704
    id(b) #2028588670992
 here, memory location is different.

 But if we assign the same in a=b way. the memory location will same.
    a = 300
    b = a
    id(a) #2028588670768
    id(b) #2028588670768
Here, memory location is same.

RULES:
    variable names are case sensitive.
    should start with letters or '_'.
    Should not create with reserved names.

Type casting :(Datatype conversion)
    Converting one datatype to another datatype.

    Types:
        implicit casting.
        explicit casting.
    implicit casting:
        Python intrepreter converts or cretes the datatype based on the given data.
    ex:
        whenever we create variable the datatype is implicitly assigned by python.

        a = 10
        type(a) # int
        a= 'ajith'
        type(a) # str
        a = '123'
        type(a) # str
        a= 1.23
        type(a) # float
    Explicit type casting:
        User forcefully converts variable datatypes to another.

    int(), str(), float()

int():
    ip - str, float
    op - int

ex :
    a ='123'
    b = 2.9 
    c = '5.62'
    x = int(a)
    y = int(b)
    z = int(c)  #error
    print(x) #123
    print(y)    #2
    print(z)

Notes:
    when converting float to int, the float is truncated into previous whole number.
    We can not convert letters to int.
    We can not use int() if string is float number i.e. '2.3'.
    To convert this,
        a = '5.62'
        x = int(float(a))
        print(x)

str():
    ip - int, float
    op - str

ex :
    a =123
    b = 2.9 
    c = '5.62'
    x = str(a)
    y = str(b)
    z = str(c) 
    print(x) #123
    print(y)    #2.9
    print(z)

float():
    ip - str, int
    op - float

ex:
    a= '2.3'
    b='2'
    c= 5 
    x = float(a)
    y = float(b)
    z = float(c) 
    print(x) #2.3
    print(y) #2.0
    print(z) #5.0
Notes:
    We can not convert letters to float.    