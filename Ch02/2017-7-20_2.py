## Ch2 P2.6
userInput = input('Please enter the measurement in meter: ')
inputMeter = float(userInput)

outputMile = inputMeter * 0.0006214
outputFeet = inputMeter * 3.2808399
outputInch = inputMeter * 39.3700787

print('%-19s %10.3f %s' %('The measurement is ', outputMile, 'mile(s)'))
print('%-19s %10.3f %s' %('The measurement is ', outputFeet, 'feet'))
print('%-19s %10.3f %s' %('The measurement is ', outputInch, 'inch(es)'))


## Ch2 P2.7
from math import *
userInput1 = input('Please enter the radius: ')
inputRadius = float(userInput1)

area = pi*inputRadius**2
circum = 2*pi*inputRadius
volume = 4*pi*inputRadius**3
surface = 4/3*pi*inputRadius**2

print('%-20s %10.2f' %('The area is ', area))
print('%-20s %10.2f' %('The circumference is', circum))
print('%-20s %10.2f' %('The volume is', volume))
print('%-20s %10.2f' %('The surface is', surface))
