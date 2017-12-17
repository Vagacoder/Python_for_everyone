## Ch04 P4.14

from math import *

x = input('please enter data: ')

if not x.isdigit():
    print('Please enter valid number')
    x = input('please enter data: ')

n = 0
sum = 0
square_sum = 0

while x != 'Q' and x!= 'q':
    xi = float(x)
    sum += xi
    square_sum += xi**2
    n += 1
    x = input('please enter data (enter Q to finish): ')

standev = sqrt(((square_sum)-sum**2/n)/(n-1))
print('Standard deviation is: %.4f' %standev)



