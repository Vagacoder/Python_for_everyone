## 

def squareArea(sideLength):
    area = sideLength **2
    return area

print(squareArea(10))

## Ch05 R5.2

def Max2Integer(a, b):
    if a == b:
        max_one = 'Same'
    elif a > b:
        max_one = a
    elif a < b:
        max_one = b
    return max_one

print(Max2Integer(3,3))

def Min3Float(a, b, c):
    if a == b and b == c:
        min_one = 'Same'
    elif a <= b and a <=c:
        min_one = a
    elif b <=c and b <=a:
        min_one = b
    elif c <=a and c <= b:
        min_one = c
    return min_one

print(Min3Float(2.1, 2.4, 2.4))

def TestPrime(a):
    count = 0
    result = False

    for i in range(1,a+1):
        if a%i == 0:
            count += 1
    if count == 2:
        result = True

    return result

print(TestPrime(1))

def checkString(string1, string2):
    if string1 in string2:
        result = True
    else:
        result = False
    return result

print(checkString('H', 'Hello World'))

def balance(inital_balance, rate, years):
    balance_1 = inital_balance * (1 + rate*0.01)**years
    return balance_1

print('%.2f'%balance(1000, 5, 3))

from random import *

def rand_int(maxNum):

    r = int(random()*maxNum)

    return r

print(rand_int(100))
