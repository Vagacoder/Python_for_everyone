## Ch04 R4.14

from math import *

firstName = input('Please enter the first name: ')
lastName = input ('Please enter the last name: ')

score = 0
count = 0
totalScore = 0

while score >= 0:
    score = int(input('Please enter the score, or enter -1 to finish: '))
    if score >= 0:
        count += 1
        totalScore += score

if count >0:
    average = totalScore/count
    print('The average score of %s %s is %.1f.' %(firstName, lastName, average))
else:
    print('No score entered.')
