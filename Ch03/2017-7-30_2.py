## Ch03 P3.9 final version
from sys import *

model1 = str(input('Please enter C for Celsius or F for Fahrenheit: ')).upper()
degree = float(input('Please enter the degree: '))

if degree <-100 or degree > 600:
    exit('Temperature is our of range, please try again.')


model2 = str(input('Please enter M for Meter or F for Feet: ')).upper()
altitude = float(input('Please enter the altitude: '))

if altitude <-50 or altitude > 20000:
    exit('Altitude is out of range, please try again.')



if model1 == 'C':
    if model2 == 'M':
        if degree > 100-(altitude/300):
            state = 'gas'
        elif degree > 0-(altitude/300):
            state = 'liquid'
        else:
            state = 'solid'
    elif model2 == 'F':
        if degree > 100-(altitude/1000):
            state = 'gas'
        elif degree > 0-(altitude/1000):
            state = 'liquid'
        else:
            state = 'solid'

    else:
        print('Wrong inputs, please try again.')


elif model1 == 'F':
    if model2 == 'M':
        if degree > 212 - (altitude / 300):
            state = 'gas'
        elif degree > 32 - (altitude / 300):
            state = 'liquid'
        else:
            state = 'solid'
    elif model2 == 'F':
        if degree > 212 - (altitude / 1000):
            state = 'gas'
        elif degree > 32 - (altitude / 1000):
            state = 'liquid'
        else:
            state = 'solid'

    else:
        print('Wrong inputs, please try again.')

else:
    print('Wrong inputs, please try again.')

if model2 == 'M':
    unit = 'Meter'
elif model2 == 'F':
    unit = 'Feet'

print('Water at %.1fø%s is %s at %.1f %s.' % (degree, model1, state, altitude, unit))