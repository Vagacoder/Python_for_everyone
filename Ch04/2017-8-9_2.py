## Ch04 P4.3

string = 'Here we are6. We are so happy3! How about you1?'

for i in string:
    if i.isupper():
        print(i, end='')

print()

for i in range(len(string)):
    if i%2 == 0:
        print(string[i], end='')

print()

for i in string:
    if i in 'aeiouy':
        print('_', end='')
    else:
        print(i, end='')

print()

count = 0
for i in string:
    if i.isdigit():
        count +=1
print(count)

print()

for i in range(len(string)):
    if string[i] in 'aeiouy':
        print(i, end=' ')

## Ch04 P4.4

highestValue = int(input("Enter a value for month #1: "))

highestMonth = 1

for currentMonth in range(2, 13):
    nextValue = int(input("Enter a value for month #%d: "%currentMonth))

    if nextValue > highestValue :
        highestValue = nextValue
        highestMonth = currentMonth

print('The highest temp is %.1f at month %d.'%(highestValue,highestMonth))

## Ch04 P4.9

string = 'We are here, and we are happy! How about you?'

for i in range(len(string)-1, -1, -1):
    print(string[i], end='')

## Ch04 P4.11
## This is not correct
string = 'harry'

count = 0
for i in range(len(string)):
    if string[i] in 'aeiouy' and i != len(string)-1:
        count += 1

if count == 0:
    count += 1

print('Word   Syllables')
print('%-7s%-2d'%(string, count))

