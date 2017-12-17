## Ch03 R3.5 R3.6

x = -2
y = 10

if x >= 0:
    y = x
else:
    y = -x

print(y)

## Ch03 P3.32

WAGE_PER_HOUR = 9.25

name = input('Please enter the name of employee: ')
hour = float(input('Please enter the hours he worked: '))

if hour <= 40:
    wage = hour * WAGE_PER_HOUR

else:
    wage = 40 * WAGE_PER_HOUR + (hour - 40)*WAGE_PER_HOUR*1.5

print('The wage of %s is $%.2f.' %(name, wage))
