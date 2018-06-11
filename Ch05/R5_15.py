# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 18:00:14 2018

@author: qhu
"""

## R5.15

#string = "goodbye"
string = "WearelikeComputerScienceAndwewillkeepstudying"

# this recursive function is using select sort
def reverse(input) :
    if len(input) == 1:
        return input
    else :
        minletter = min(input)
        result = minletter + reverse(input.replace(minletter, "", 1))
        return result
        
print(reverse(string))