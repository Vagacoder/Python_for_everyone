## Ch04 tripinv

RATE = 10.0
INI_BALANCE = 10000.0
TARGET = 2 * INI_BALANCE

balance = INI_BALANCE

year = 0

while balance < TARGET:
    year += 1
    balance = balance * (100 + RATE)/100
    print('The balance after year',year, 'is $%.2f' %balance)

print(year)

## Ch04 R4.1
from math import *

INI_num1 = 0
#square_num = 0

n = int(input('Please enter a number: '))

while INI_num1 < sqrt(n)-1:
    INI_num1 += 1
    square_num1 = INI_num1 **2
    print(square_num1)

print()

INI_num2 = 0
num2 = 0

while num2 < n-10:
    INI_num2 += 1
    num2 = INI_num2 * 10
    print(num2)

print()
INI_num3 = 0
num3 = 0

while INI_num3 < log(n, 2)-1:
        INI_num3 += 1
        num3 = 2 ** INI_num3
        print(num3)

