from math import *

x = sqrt(2)
y = 2.0

if x * x == y:
    print('sqrt(2) times sqrt(2) is 2')

else:
    print('sqrt(2) times sqrt(2) is not 2 but %.18f' % (x*x))

EPSILON = 1E-14
print(EPSILON)

if abs(x*x - y) < EPSILON:
    print('sqrt(2) times sqrt(2) is approximately 2')

s ='120'
t= '20'

if s == t:
    comparison = 'is the same as'
else:
    comparison = 'is not the same as'

print('The string "%s" %s the string "%s".' %(s, comparison, t))

u = '1' + t

if s!= u:
    comparison = 'not'
else:
    comparison = ''

print('The string "%s" and "%s" are %sidentical.' %(s, u, comparison))

## Ch03 R3.4

n = 1
m = -1

if n < -m :
    print(n)
else :
    print(m)

n = 1
m = -1

if -n >= m :
    print(n)
else :
    print(m)

x = 0.0
y = 1.0
if abs(x - y) < 1 :
    print(x)
else :
    print(y)

x = sqrt(2.0)
y = 2.0
if x * x == y :
    print(x)
else :
    print(y)

## Ch03 R3.7

x = 10
y = 10.2

if x == 10:
    print('x is 10')

if y == 10.2000:
    print('y is 10.2')

if (y**2)**(1/2) == 10.2:
    print(type(y), ' y is 10.2')

else:
    print((y**2)**(1/2), 'y is not 10.2')