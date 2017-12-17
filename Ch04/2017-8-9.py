## Ch04 R4.2

num_a = 0
total_a = 0

while num_a < 100:
    num_a += 2
    total_a += num_a

print(total_a)
#print((2+100)*50/2)

##=============
num_b = 0
total_b = 0

while num_b**2 <100:
    num_b += 1
    total_b += num_b**2

print(total_b)
#print(1+4+9+16+25+36+49+64+81+100)

##=============
#a = int(input('please enter number a: '))
a =3
#b = int(input('please enter number b: '))
b =5
num_c = min(a, b)-1
total_c = 0

while num_c < max(a, b):
    num_c += 1
    if num_c %2 == 1:
        total_c += num_c

print(total_c)

##=========
num_d = input('please enter a number: ')

count = 0
total_d = 0
while count < len(num_d):
    if int(num_d[count])%2 ==1:
        total_d += int(num_d[count])

    count += 1

print(total_d)

##
total_d1 = 0
for i in num_d:
    if int(i)%2 == 1:
        total_d1 += int(i)

print(total_d1)

##R4.12
count = -2

for i in range(1,7):
    for j in range(1,8):
        if i == 1 and j == 1:
            print(' Su   M   T   W  Th   F  Sa')

        if count <=0 or count>31:
            print('   ', end=' ')
        elif count > 0:
            print('%3d'%count, end=' ')
        count +=1
    print()

##R4.13
for i in range(1,14):

    if i == 1:
        print('Celsius | Fahrenheit')
    elif i == 2:
        print('--------+-----------')
    elif i >=3:
        cel = (i-3)*10
        fah = cel*9/5 +32
        print('%7d | %10d'%(cel, fah))