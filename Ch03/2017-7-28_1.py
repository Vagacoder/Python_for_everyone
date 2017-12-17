## Ch03 R3.9

x = input('Please enter x axis (a, b, ... g, h): ')
y = int(input('Please enter y axis (1-8): '))

#x = 'g'
#y = 5

if x == 'a' or x == 'c' or x == 'e' or x =='g':
    if y%2 == 1:
        #print('The grid is black')
        color = 'black'
    else:
        #print('The grid is white')
        color = 'white'

else:
    if y%2 == 1:
        #print('The grid is white')
        color = 'white'
    else:
        #print('The grid is black')
        color = 'black'

print('The grid \"%s%d\" is %s.' %(x, y, color))

## Ch03 P3.20

#month = int(input('Please enter number for month (1-12): '))
#day = int(input('Please enter number of day (1-31): '))

month = 6
day = 21

monthList = ['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

if month == 1 or month == 2 or month == 3:
    season = 'Winter'

elif month == 4 or month == 5 or month == 6:
    season = 'Spring'

elif month == 7 or month == 8 or month == 9:
    season = 'Summer'

elif month == 10 or month == 11 or month == 12:
    season = 'Fall'

if month%3 == 0 and day >= 21:
    if season == 'Winter':
        season = 'Spring'
    elif season == 'Spring':
        season = 'Summer'
    elif season == 'Summer':
        season = 'Fall'
    elif season == 'Fall':
        season = 'Winter'

print(monthList[month],day,'is',season)

## Ch03 P3.23

RATE1 = 0.01
RATE2 = 0.02
RATE3 = 0.03
RATE4 = 0.04
RATE5 = 0.05
RATE6 = 0.06

#income = int(input('Please enter your income (in dollars): '))

income = 70000

if income <= 50000:
    tax = income * RATE1

elif income <= 75000:
#if income > 50000 and income <= 75000:
    tax = 50000 * RATE1 + (income - 50000) * RATE2

#elif income > 75000 and income <= 100000:
elif income <= 100000:
    tax = 50000 * RATE1 + 25000 * RATE2 + (income - 75000) * RATE3

#elif income > 100000 and income <= 250000:
elif income <= 250000:
    tax = 50000 * RATE1 + 25000 * RATE2 + 25000 * RATE3 + (income - 100000) * RATE4

#elif income > 250000 and income <= 500000:
elif income <= 500000:
    tax = 50000 * RATE1 + 25000 * RATE2 + 25000 * RATE3 + 150000 * RATE4 + (income - 250000) * RATE5

elif income > 500000:
    tax = 50000 * RATE1 + 25000 * RATE2 + 25000 * RATE3 + 150000 * RATE4 + 250000 * RATE5 + (income - 500000) * RATE6

print('Your tax is: $%.2f' %tax)


