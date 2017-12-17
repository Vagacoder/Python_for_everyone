## Ch02 P2.3

from math import *

inputNum = input('Please enter an integer: ')

try:
    number = int(inputNum)

    print('The square of '+str(number)+' is',number*number)

    print('The cube of '+str(number)+' is '+str(number*number*number))

    print('The forth power of '+str(number)+' is '+str(number**4))

except:
    print('Wrong data type, please try again')

## Ch02 P2.5

print('%-11s%10d'%('Sum:',45))
print('%-11s%10d'%('Difference:',-5))
print('%-11s%10d'%('Product:',500))
print('%-11s%13.2f'%('Average:',22.50))

## Ch02 P2.8

length = float(input('Please enter the length of rectangle: '))
width = float(input('Please enter the width of rectangle: '))

area = length*width
perimeter = 2*(length + width)
diagonal = sqrt(length**2 + width**2)

print('The area is', area)
print('The perimeter is', perimeter)
print('The diagonal is %.4f' %diagonal)
