## Ch1 R2.15
from math import *

n = int(input())
print(n)

lastDigit = n%10
digits = int(log(n, 10))
print(digits)

firstDigit = n//10**(digits)

print('The last digit is', lastDigit)
print('The first digit is', firstDigit)

#-------------
## Ch1 R2.17

r1 = 8
r2 = 10
r3 = 5
r4 = 4

h1 = 30
h2 = 12
h3 = 12

v1 = pi/3 * h1 * (r1**2 + r1*r2 + r2**2)
v2 = pi/3 * h2 * (r2**2 + r2*r3 + r3**2)
v3 = pi/3 * h3 * (r3**2 + r3*r4 + r4**2)
v = v1 + v2 + v3

print(v1)
print(v2)
print(v3)
print(v)

#------------
