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
d = {'a':10, 'b':1, 'c':22}
print(type(d.items()))
t = list(d.items())
print(t)
t.sort()
print(t)



