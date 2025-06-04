try and except

Used to handle the error.

try - Executed the codes for error.
except -  This block will be executed when there is an error in try block.
else - this block executed when there is no error in try block
finally - executes regardless of try,except,else blocks

print(xyz) # it will throw error because xyz is not defined.

try:
    print(xyz)
except:
    print("xyz define pannuda venna") # this code will executed

There are many Exceptions available in python:
'''
SyntaxError: This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.
TypeError: This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.
NameError: This exception is raised when a variable or function name is not found in the current scope.
IndexError: This exception is raised when an index is out of range for a list, tuple, or other sequence types.
KeyError: This exception is raised when a key is not found in a dictionary.
ValueError: This exception is raised when a function or method is called with an invalid argument or input, such as trying to convert a string to an integer when the string does not represent a valid integer.
AttributeError: This exception is raised when an attribute or method is not found on an object, such as trying to access a non-existent attribute of a class instance.
IOError: This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.
ZeroDivisionError: This exception is raised when an attempt is made to divide a number by zero.
ImportError: This exception is raised when an import statement fails to find or load a module.
'''
try:
    print(5/0)
except ZeroDivisionError:
    print("number can not be devided by zero")

# same as:
try:
    print(5/0)
except :
    print("number can not be devided by zero")

try:
    prin("ajith")
except SyntaxError:
    print("Syntax olunga podu da")
except:
    print("nothing")
'''
SyntaxError: This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.
TypeError: This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.
NameError: This exception is raised when a variable or function name is not found in the current scope.
IndexError: This exception is raised when an index is out of range for a list, tuple, or other sequence types.
KeyError: This exception is raised when a key is not found in a dictionary.
ValueError: This exception is raised when a function or method is called with an invalid argument or input, such as trying to convert a string to an integer when the string does not represent a valid integer.
AttributeError: This exception is raised when an attribute or method is not found on an object, such as trying to access a non-existent attribute of a class instance.
IOError: This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.
ZeroDivisionError: This exception is raised when an attempt is made to divide a number by zero.
ImportError: This exception is raised when an import statement fails to find or load a module.
'''

def nullfunc(a,b):
    try:
        c=a+b
    except TypeError:
        print("Please enter numbers only")
    else:
        print(c)
    finally:
        print("Operation is successfull")

nullfunc(10,"ajith")
nullfunc(5,5)