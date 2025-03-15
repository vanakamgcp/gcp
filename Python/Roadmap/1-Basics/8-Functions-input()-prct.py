# run this file in CLI as follows
# python .\8-Function-sample.py 10 20 30

from sys import argv

print("Total argument passed :", len(argv))

# to print the arg passed
for i in argv:
    print(i)

# print(argv[3]) # if index is out of range it will throw the same error