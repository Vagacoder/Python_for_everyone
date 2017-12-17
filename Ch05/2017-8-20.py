## Ch05 P 5.3

def firstDigit(number):
    count = 0
    for a in str(number):
        if a.isdigit():
            count += 1
    return count

print(firstDigit('3w3fge5q1'))

## Ch05 P 5.8
from random import *

def scramble(word):
    if len(word) <= 3:
        return word
    elif len(word) > 3:
        a = randint(1,len(word)-2)
        b = randint(1,len(word)-2)
        while a == b:
            b = randint(1, len(word) - 2)
        print(a,b)
        x = min(a, b)
        y = max(a, b)
        new_word = word[0:x] + word[y] + word[x+1:y] + word[x] + word[y+1:]

    return new_word

print(scramble('word'))