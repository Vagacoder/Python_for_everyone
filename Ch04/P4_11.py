# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 15:30:08 2018

@author: qhu
"""

# P4.11
str1 = "the"
count = 0
wasVowel = False

for i in range(len(str1)):
    if not wasVowel:
        if str1[i].lower() in "aiouy":
            count += 1
            wasVowel = True
        if str1[i].lower() in "e" and i != len(str1)-1:
            count += 1
            wasVowel = True
    else:
        if str1[i].lower() not in "aeiouy":
            wasVowel = False

if wasVowel == 0:
    count = 1

print('Word   Syllables')
print('%-7s%-2d'%(str1, count))
        
    