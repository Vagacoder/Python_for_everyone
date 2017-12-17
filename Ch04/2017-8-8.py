## Ch04 R4.26

for i in range(3):
    for j in range(4):
        print('*', end='')
    print()

print()
for i in range(3):
    print('*'*4, end= '')
    print()

## Ch04 P4.18

for i in range(1,11):
    for j in range(1,11):
        print('%4d'%(i*j), end='')
    print()

## Ch04 P4.22
num = int(input('Please enter an integer: '))

for i in range(1,num+1):
    print(' '*(num-i) + '*'*(2*i-1), end='')
    print()

for i in range(num-1,0,-1):
    print(' ' * (num - i) + '*' * (2 * i - 1), end='')
    print()
    #print(i)

##SC
upper = 0
vowel = 0

a = 'We are soldiers! We..... WILL NOT surrender.'

for i in a:
    if i.isupper():
        upper += 1
    if i.lower() in 'aeiou':
        vowel += 1
print(upper)
print(vowel)

string = '488-2495-28 172-195 73'
new_string1 = string.replace('-','')
new_string2 = new_string1.replace(' ','')
print(new_string2)

## SC4.35
position = 0
count = 0
while position < len(a) and count<2:
    if a[position].isupper():
        count += 1
    position += 1

if count == 2:
    print(a[position-1])

else:
    print('No 2 uppercase letters.')

## SC4.36
position = 0

while position < len(a):
    if a[position] in '.?!,;:\'':
        print('%d: %s' %(position+1, a[position]))
    position += 1

for i in range(len(a)):
    if a[i] in '.?!,;:\'':
        print(i+1,':', a[i])