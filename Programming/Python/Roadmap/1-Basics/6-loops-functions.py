zip(list1,list2)
The zip() function returns a zip object, 
which is an iterator of tuples where the first item in each passed iterator is paired together, 
and then the second item in each passed iterator are paired together etc.

If the passed iterators have different lengths, the iterator with the least items decides 
the length of the new iterator.

a = ["John", "Charles", "Mike"]
b = ["Jenny", "Christy", "Monica"]
c = ["aji", "abi", "moni"]

x = zip(a, b,c)
print(x)
type(x)
for i in x:
    print(i).

for i,j,k in x:
    print(i,j,k,sep="-")

enumerate(list1)