#String Is a set of sequence
#String is immutable(We cant change it)
#String support slicing (Slicing dont give error)
    # 1.) Negative Slicing
    # 2.) Positive Slicing
#String support indexing (Indexing start 0)
#Constructor of string is str()

a="Deepak" #Indexing
print(a)
print(a[0])
print(a[-3])
print(a[2:5]) #Slicing
print(a[2:5:1])
print(a[2:5:2])
print(a[0:6])

b="wekjnrkjrenefdn4jkeriwekjfkwnerwne"
print(b[0::2])
print(len(b))

c="0123456789"
print(c[1::2])
print(c[9::-1])
print(c[:])

d="Deepak" #Negative Indexing
print(d[-6::1])
print(d[-1::-1])

str()
print(id(""))

print(id(d[3]))