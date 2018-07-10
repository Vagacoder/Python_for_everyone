# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 17:08:27 2018

@author: qhu
"""

# P11.5

def reverse(text):
    result = ""
    for i in range(len(text)-1, -1 , -1):
        result += text[i]
    return result
    

def main():
    print(reverse("Hello!"))
    
    
main()