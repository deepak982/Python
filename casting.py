a="10"
print(type(a))
print(type(int(a)))

b="10.0"
print(int(float(b)))

c=(1,2,3,4)
print(list(c))

d={1,2,3,4,5}
d.update((2,3,4))
print(d)