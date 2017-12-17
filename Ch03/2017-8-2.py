from math import *

EPSILON =1E-14

#x = float(input('Please enter a number: '))

x=10.001
y = 10.0

print(abs(x-y))

if abs(x-y) < EPSILON:
    print('the number is close to 10.')

else:
    print('the number is different from 10.')

## Ch03 R3.18
from sys import *

#score_raw = input('Please enter the score: ')

score_raw = '87'

if not score_raw.isdigit():
    exit('Wrong input, please try again.')

score = int(score_raw)

if score < 0 or score >100:
    exit('Wrong score range, please input socre in 0-100.')


if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print('The grade is %s.' %grade)

## Ch03 R3.25


p = True
q = True
r = True

print((p and q) or not r)
print(not (p and (q or not r)))


## Ch03 R3.28
b = False
x = 0

print()
print(b and x == 0)
print(b or x == 0)
print(not b and x== 0)
print(not b or x== 0)
print(b and x!=0)
print(b or x != 0)
print(not b and x !=0)
print(not b or x !=0)

## Ch03 P3.2

#num = float(input('Please enter a float number: '))

num = 2

if num == 0 :
    print('zero')

if num > 0 :
    print('positive')
if num < 0:
    print('negative')

if abs(num) < 1:
    print('less than 1')

if abs(num) > 1000000:
    print('large')


## Ch03 P3.3
#num = int(input('Please enter an integer: '))

if num <0:
    num = -num
    print(num)

num_len= round(log(num,10))+1
print(num_len)

## Ch03 P3.4

num1 = int(input('Please enter first number: '))
num2 = int(input('Please enter second number: '))
num3 = int(input('Please enter third number: '))

if num1 == num2 and num2 == num3:
    print('all same')

elif num1 != num2 and num2 != num3 and num1 != num3:
    print('all different')

else:
    print('neither')

if num1 > num2 and num2 > num3:
    print('decreasing')

elif num1 < num2 and num2 < num3:
    print('increasing')

else:
    print('neither')


