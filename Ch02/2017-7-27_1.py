## Ch02 P2.33

#number = input('Please enter 10 digits number: ')
number = '8055693215'
print('(' +number[0] +number[1] +number[2] +')' +number[3] +number[4] +number[5] +'-' +number[6] +number[7] \
      +number[8] +number[9])

## Ch02 P2.34

#pay = float(input('Please enter the pay: '))
pay =5.34
pay1 = int(pay*100)

dollar = pay1//100
cent = pay1%100

print('Dollar: %5d' %dollar)
print('Cent:   %5d' %cent)


## Ch02 P2.36

#initial = int(input('Please enter initial balance: '))
initial = 2000

#interestRate = int(input('Please enter interest rate: '))
interestRate = 8

firstBalance = initial *(1+(interestRate/12*0.01))
secondBalance = firstBalance *(1+(interestRate/12*0.01))
thirdBalance = secondBalance *(1+(interestRate/12*0.01))

print('After first month:  %10.2f' %firstBalance)
print('After second month: %10.2f' %secondBalance)
print('After third month:  %10.2f' %thirdBalance)

## Ch02 P2.37

#rental = int(input('Enter the number of movie rentals: '))
#refer = int(input('Enter the number of member referred: '))

rental = 56
refer =15

print('The discount is:   %6.2f percent' %(min(75, rental+refer)))

## Ch02 P2.39
from math import *

relative_humidity = float(input('Please enter the relative humidity: '))
temperature = float(input('Please enter the temperature (degree C): '))
A = 17.27
B = 237.7

dew_point = (A * temperature)/(B + temperature) + log(relative_humidity)

print('Dew point is:%6.1f degree C.' %dew_point)

## Ch02 P2.40
