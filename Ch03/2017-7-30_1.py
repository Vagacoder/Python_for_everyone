## Ch03 P3.39


#month = int(input('Please enter the month (1 for January, 2 for February): '))

month = 1

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print('31 days')

elif month == 4 or month == 6 or month == 9 or month == 11:
    print ('30 days')

else:
    print('28 or 29 days')

## Ch03 SC36

theString = 'we_are_soldiers456.'

print(theString.count(' '))

print(theString[0].isupper())

if theString.islower() and theString.isalpha:
    print('Only lower case letters method1')

if theString.islower() and theString.count(' ')==0:
    print('Only lower case letters method2')

if theString.isdigit():
    print('Only number')

from math import *
x = 2
y = 1

if 1 + x > x**sqrt(2):
    y = y + x
    print(y)
    print(x**sqrt(2))