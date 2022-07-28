# Tuple is a set of sequence of elements
# Tuple is immutable
# Tuple follow Indexing
# Tuple follow slicing
# Tuple constructor is tuple()
# To create empty tuple use ()

# Tuple Faster then list

a=tuple()          # tuple not use to make variable
print(type(a))

b=()
print(type(b))

c=(1,2,3,4,"Deepak",10.9)
print(c)

c.count(2)

c.index(2)


print(c[4])
print(c[4][0])
print(c[1:5])           # Slicing

# Use Case:-

d=1
print(type(d))

a=["Krishna","Deepak","Rahul"]          # List
print(type(a))
a.append("Rohan")
print(a)

b=("Krishna","Deepak","Rahul")          # Tuple
print(type(b))
