# dict constructor is dict()
# dict literal is {}
# dict is a combination of keys and values
# dict is mutable
# {} Curly Bracket use for dictionary not for set

a=dict()
print(type(a),a, sep="\n")

b={}
print(type(b),b, sep="\n")

c={1:"Krishna",2:"Deepak",3:"Rohit"}
print(c)
print(c[2])

c.update({4:"Kashish"})
print(c)

d=c.keys()
print(d)

e=c.values()
print(e)

f=c.items()
print(f)

c.pop(2)         # Pop use for remove item
print(c)

c.popitem()     # Popitem use for remove last value
print(c)

g=c.get(4,"Number 4 argument not available")
print(g)

c[1]={1:"Sonali",2:"Alex"}
print(c)

c[1][2]={3:"Radhika",4:"Manish"}
print(c)

c[3]={1,2,3,4,5,6,7,8,9,10}
print(c)

x=c
x.update({8:"gandhi"})
print(x,c, sep="\n")

x=c.copy()
x.update({7:"Kanika"})
print(x,c, sep="\n")