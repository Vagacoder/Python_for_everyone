## Ch1 R2.18
from math import *

diameter = 12
chord = 10

h = (diameter/2) - sqrt((diameter/2)**2 - (chord/2)**2)
print(h)

area = 2/3*chord*h + h**3/2/chord

print('The area is about', area, 'inch^2')
print(pi/2*(diameter/2)**2)
