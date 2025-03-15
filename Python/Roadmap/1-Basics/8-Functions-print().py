# output() in python
print() is used to display the output msg.

print('tony','banner','peter') # tony banner peter

# Above values are seperated by SPACE by default.

# if we want to change the seprator use 'sep'

print('tony','banner','peter',sep='-')

output formatting.

1.op_str.format(*args,**kwargs)

print("My name is {}.I am from {}".format('ajith','chennai'))

print("My name is {0}.I am from {1}".format('ajith','chennai'))
# the op is reversed for below
print("My name is {0}.I am from {1}".format('chennai','ajith'))

fname='ajith'
lname='j'
cmpny='accenture'

print('{},{} is working in {}'.format(fname,lname,cmpny))
# access values by name in print
print("My first name is {first_name} and last name is {last_name}".format(first_name=fname,last_name=lname))

# to display '+','-' signs
for pos and neg numbers :
    {:+f}
for neg numbers only:
    {:-f}

posnum= float(+2.6)
negnum=float(-1.2)

print("postive no : {},Negative no: {}".format(posnum,negnum))

print("postive no : {:+f},Negative no: {:+f}".format(posnum,negnum))