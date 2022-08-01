# String is not a set of sequence of element
# Set constructor is set()
# Set dose not contain literal
# Set use hassing concept
# Set dosenot allow duplicate values
# Set is mutable

a = set()  # Set contain immutable object
print(a)

b = {1, 2, 3, 4, 4, 4, 5, 5}
print(type(b),b)

c={1,2,3,4,(6,7,8,9),"Deepak"}       # (6,7,8,9) This is tuple , tuple is immutable
print(c)                             # "Deepak" This is string , String is immutable

# d={1,2,3,4,[5,6,7]}                  # You can not add list in set because list is mutable , they give you TypeError: unhashable type: 'list'
# print(d)

a={1,2,3,4}
b={3,4,5,6,7}

a.add((5,6,7,8))
print(a)

a.add("Deepak")
print(a)

a.clear()
print(a)

a.update((9,8,7,6,5,4))
print(a)

a.remove(6)
print(a)