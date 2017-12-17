## Ch02 2.19 2.20

month = ' January   February  March     Apriel    May       June      July      August    September October   November  December  '

#num = int(input('Please enter month: '))
num = 3
num1 = num*10

print(month[num1-9]+month[num1-8]+month[num1-7]+month[num1-6]+month[num1-5]+ \
      month[num1-4]+month[num1-3]+month[num1-2]+month[num1-1]+month[num1])

## Ch02 P2.20
print('       /\\')
print('      /  \\')
print('     /    \\')
print('    /      \\')
print('    --------')
print('      "  "  ')
print('      "  "  ')
print('      "  "  ')
print('      "  "  ')
print('      "  "  ')

## Ch02 P2.21

y = int(input('Please enter the year (1800-2001): '))
a = y%9
b = y//100
c = y%100
d = b//4
e = b%4
g = (8*b+13)//25
h = (19*a+b-d-g+15)%30
j = c//4
k = c%4
m = (a+11*h)//319
r = (2*e + 2*j - k -h +m +32)%7
n = (h -m +r +90)//25
p = (h -m +r +n +19)%32

print(n, p)
num1= n*10

monthEaster = month[num1-9]+month[num1-8]+month[num1-7]+month[num1-6]+month[num1-5]+ \
      month[num1-4]+month[num1-3]+month[num1-2]+month[num1-1]+month[num1]

print(monthEaster.replace(' ',''),p)