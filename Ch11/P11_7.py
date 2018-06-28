# -*- coding: utf-8 -*-
## P11.6 and P11.7
#

# P11.6
def find(text, string):
    if len(text) < len(string):
        return False    
    else:
        if text.startswith(string):
            return True
        else:
            newText = text[1:]
            return find(newText, string)

# P11.7
def indexOf(text, string):
    print(findIndex(text, string, 0))

# helper function for indexOf()
def findIndex(text, string, index):
    if index + len(string) > len(text):
        return -1
    else:
        newText = text[index:]
        if newText.startswith(string):
            return index
        else:
            return findIndex(text, string, index + 1 )
        
    
def main():
    print(find("Mississippi", "sip"))
    indexOf("Mississippi", "sip")
    
    
main()