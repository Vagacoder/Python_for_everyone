## Ch03 R3.22

#x = input('Please enter a, b, c or d: ')
x = 'a'

if x == 'a':
    print('It is A.')

elif x == 'c':
    print('It is C.')

elif x == 'b':
    print('It is B.')

else:
    print('It is D.')

## Ch03 P3.9
from sys import *

model1 = str(input('Please enter C for Celsius or F for Fahrenheit: ')).upper()
degree = float(input('Please enter the degree: '))

if degree <-100 or degree > 600:
    exit('Temperature is our of range, please try again.')


model2 = str(input('Please enter M for Meter or F for Feet: ')).upper()
altitude = float(input('Please enter the altitude: '))

if altitude <-50 or altitude > 20000:
    exit('Altitude is out of range, please try again.')

#model = 'C'
#degree = 85

if model1 == 'C':
    if model2 == 'M':
        if degree > 100-(altitude/300):
            print('Water at %.1føC is gas at %.1f meters.' %(degree, altitude))
        elif degree > 0-(altitude/300):
            print('Water at %.1føC is liquid at %.1f meters.' %(degree, altitude))
        else:
            print('Water at %.1føC is solid at %.1f meters.' %(degree, altitude))
    elif model2 == 'F':
        if degree > 100-(altitude/1000):
            print('Water at %.1føC is gas at %.1f feet.' %(degree, altitude))
        elif degree > 0-(altitude/1000):
            print('Water at %.1føC is liquid at %.1f feet.' %(degree, altitude))
        else:
            print('Water at %.1føC is solid at %.1f feet.' %(degree, altitude))

    else:
        print('Wrong inputs, please try again.')


elif model1 == 'F':
    if model2 == 'M':
        if degree > 212 - (altitude / 300):
            print('Water at %.1føF is gas at %.1f meters.' % (degree, altitude))
        elif degree > 32 - (altitude / 300):
            print('Water at %.1føF is liquid at %.1f meters.' % (degree, altitude))
        else:
            print('Water at %.1føF is solid at %.1f meters.' % (degree, altitude))
    elif model2 == 'F':
        if degree > 212 - (altitude / 1000):
            print('Water at %.1føF is gas at %.1f feet.' % (degree, altitude))
        elif degree > 32 - (altitude / 1000):
            print('Water at %.1føF is liquid at %.1f feet.' % (degree, altitude))
        else:
            print('Water at %.1føF is solid at %.1f feet.' % (degree, altitude))

    else:
        print('Wrong inputs, please try again.')

else:
    print('Wrong inputs, please try again.')

## Ch03 P3.34

COUPON1 = 8
COUPON2 = 10
COUPON3 = 12
COUPON4 = 14

#cost = float(input('Please enter the cost of your groceries: '))
cost = 200

if cost > 210:
    #print('You win a discount coupon of %.2f. (%d%% of your purchase)' % (cost * COUPON4 /100, COUPON4))
    coupon = COUPON4

elif cost > 150:
    #print('You win a discount coupon of %.2f. (%d%% of your purchase)' % (cost * COUPON3 / 100, COUPON3))
    coupon = COUPON3

elif cost > 60:
    #print('You win a discount coupon of %.2f. (%d%% of your purchase)' % (cost * COUPON2 / 100, COUPON2))
    coupon = COUPON2

elif cost > 10:
    #print('You win a discount coupon of %.2f. (%d%% of your purchase)' % (cost * COUPON1 / 100, COUPON1))
    coupon = COUPON1

else:
    #print('You don\'t have any discount for this purchase.')
    coupon = 0

print('You win a discount coupon of $%.2f. (%d%% of your purchase)' % (cost * coupon / 100, coupon))