## Ch02 R2.5
x = 2.5
y = -1.5
m = 18
n =4

from math import *

print(x+n*y-(x+n)*y)
print(m//n+m%n)
print(1-(1-(1-(1-(1-n)))))
print(sqrt(sqrt(n)))

## Ch02 R2.6

m = 18
n = 17

print(n//10 + n%10)
print(n%2 + m%2)
print((m+n)//2)
print((m+n)/2.0)
print(int(0.5*(m+n)))
print(int(round(0.5*(m+n))))

## Ch02 R2.7

s = 'Hello'
t = 'World'

print()
print(len(s)+len(t))
print(s[1]+s[2])
print(s[len(s)//2])
print(s + t)
print(t + s)
print(s*2)

## Ch02 R2.8
x=2
int(x)
print(x, 'squared is', x*x)
xcubed = x**3

## Ch02 R2.9
x =2
y =4
print('The product of ', x, 'and', y, 'is', x*y)
print('The root of difference is ', sqrt(abs(x-y)))

## Ch02 R2.10
purchase = 19.93
payment = 20.00
change = payment-purchase
print(round(change,2))
print('%.2f' %change)

## Ch02 R2.13
#word = input('Please enter a word: ')
#firstLetter = word[0]
#lastLetter = word[len(word)-1]
#middleLetter = word[(len(word)-1)//2]
#print(firstLetter, middleLetter, lastLetter)

## Ch02 R2.14
#name = input('Please enter your name: ')
name = 'Qirui Hu'
namelist = name.split(' ')
#print(namelist)
firstName = namelist[0]
if len(namelist) == 3:
    middleName = namelist[1]
    lastName = namelist[2]
    print(firstName[0]+middleName[0]+lastName[0])

elif len(namelist)== 2:
    print(namelist[0][0] + namelist[1][0])

## Ch02 R2.15

#number = int(input('Please enter a number: '))
number = 2018485
firstDigit = number//(10**int(log(number, 10)))
lastDigit = number%10

print('Fisrt digit is : %d' %firstDigit)
print('Last digit is :  %d' %lastDigit)

## Ch02 R2.16
pay = int(float(input('Please enter your payment: '))*100)
price = int(float(input('Please enter the price: '))*100)
change = pay - price
print(change)

if change >= 0:
    dollar = change//100
    print(dollar)
    print(change-dollar*100)

    quarter = (change-dollar*100)//25
    print(change-dollar*100-quarter*25)

    dimer = (change-dollar*100-quarter*25)//10
    print(change-dollar*100-quarter*25-dimer*10)

    nickel = (change-dollar*100-quarter*25-dimer*10)//5
    print(change-dollar*100-quarter*25-dimer*10-nickel*5)

    penny = (change-dollar*100-quarter*25-dimer*10-nickel*5)//1
    print('Dollar:  %d'%dollar)
    print('Quarter: %d'%quarter)
    print('Dimer:   %d' %dimer)
    print('Nickel:  %d' %nickel)
    print('Penny:   %d' %penny)

elif change<0:
    print('Payment is not enough, please retry.')



