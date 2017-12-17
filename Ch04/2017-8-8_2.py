## Random, find value of Pi

from random import *

hit = 0
count = 0

while count < 1000:
    rand1 = random()
    rand2 = random()

    x = rand1 * 2 - 1
    y = rand2 * 2 - 1

    if (x ** 2 + y ** 2) < 1:
        hit += 1
    count += 1

print(count)
print(hit)
print(hit/count*4)

## Ch04 R4.27

for i in range(3):
    hour = randint(0,12)
    min = randint(0,59)

    print('%02d:%02d'%(hour,min))

## Ch04 P4.7

## word = input('Please enter a word: ')
word = 'abcdefghijklmnopqrst'
new_word = word

for k in range(len(word)):
    i = randint(0,len(word)-2)
    j = randint(i+1,len(word)-1)

    new_word = new_word[0:i] + new_word[j] + new_word[i+1:j] + new_word[i] + new_word[j+1:len(word)]

print(new_word)