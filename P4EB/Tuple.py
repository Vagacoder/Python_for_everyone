## tuple

# tuple is a comma-separated list
t1 = 'a','b','c','d','e'
print(t1)

t2 = 'a'
print(type(t2))

t3 = 'a',
print(type(t3))

t4 = tuple('a')
print(type(t4))

t5 = tuple()
print(type(t5))

t6 = tuple('Hello World')
print(t6)

# tuple is immutable
try:
    t6[0]= 'A'
except:
    print('can\'t change tuple')

# make a new tuple to replace

t6 = ('A',) + t6[1:]
print(t6)

# comparison tuples
print((0, 1, 2) < (0, 3, 4))
print((0, 1, 1000000) < (0, 3))

# tuple assigment, the number of both sides must be same
x, y, z, u, v = t1
print(x)
print(y)
print(z)
print(u)
print(v)

addr = 'vip@here.org'
name, domain = addr.split(sep='@')
print(name)
print(domain)

# dictionary method items() return a list of tuples.
# each tuple is a pair of key-value
d = {'b':1, 'a':10, 'e':4, 'c':22, 'd':3 }
print(type(d.items()))
t = list(d.items())
print(t)
t.sort()
print(t)

# traversal keys and values in dictionary
# element in list(d.items() is a tuple
# first loop using a tuple to traversal tuples in list
for (k, v) in list(d.items()):
    print(k, v)
    print(v, k)  # the order of tuple doesnt matter

# second loop using one var to traversal tuples in list
for i in list(d.items()):
    print(i)

# value-key in dictionary can be sorted
l = list()
for k, v in list(d.items()):
    l.append((v, k))
print(l)
l.sort()
print(l)

# using tuple as key in dictionary
compD = dict()
compD['Jack','Slate'] = 1200
compD[2, 5] = 1300
compD[3] = 1400
compD['Washington', 'DC', 'USA'] = 1500
print(compD)
print(compD[2, 5])
for k in compD:
    print(k, compD[k])

# tuple is immutable, it has no methods like sort() or reverse()
# but 
a = (2, 4, 3, 1, 6)
print(a)
print(sorted(a))
print(a)





