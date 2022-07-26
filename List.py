# List is asset of sequence of elements (Each elements have either multiple data type of same data type )
# List is numtable (We can do change in list)
# List follow indexing
# List flow slicing
# List constructor is"list()"
# An empty list can also create useing "[]"
# List is called an array because python dosenot have array concept
# Concept of deep copy and shallow copy

a = [1, 2, 3, 4, 5, 6]
print(type(a))
print(a)

# create an empty list

c = list()  # Create empty list useing constructor
print(c)

e = [2, 3, 4, 1, 2, 3, 9]  # list follow indexing
print(e[2])
print(type(e[2]))
print(e[1:6])
print(e[-1::-1])

h = []
print(h)
h.append(100)  # append use for add value , appand not use in string (List is mutable) ( String is inmutable) (* concant for adding)
print(h)

d=[1,2,3,4,[5,6,7,8]]
print(d[4])
print(d[4][1])
print(id(d[4][1]))

a=[1,2,3,4]        #Shallow copy
b=a
print(a)
print(b)

b.append(100)
print(b)
print(a)

c=[1,6,5,3,2,3]
d=c
print(c)
print(d)

d=c.copy()           #Deep copy
print(d)

d.append(100)
print(c)
print(d)

x=[1,2,3,4,5]
x.append(6)
print(x)
x.extend([7,8])
print(x)
x.remove(1)
print(x)
x.insert(0,1)
print(x)

list1 = [100, 200, 300, 400, 500]
print(list1[-1::-1])
list1.reverse()
print(list1)

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3=[i+j for i, j in zip(list1,list2)]
print(list3)

list1 = [[10, 20, 30, 40]]
list2 = [100, 200, 300, 400]