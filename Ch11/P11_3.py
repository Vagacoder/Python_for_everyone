# -*- coding: utf-8 -*-

## P11.3 and P11.4

# P11.3
def reverse(text):
    
    if len(text) <= 1:
        return text
    else:
        newText = text[1:]
        return reverse(newText) +  text[0]


# P11.4
def reverse1(text, index):
    
    if index >= len(text):
        return ""
    elif (index == len(text)-1):
        return text[index]
    else:
        return reverse1(text, index+1) + text[index]


def main():
    str1 = "Hello!"
    print(reverse(str1))
    print(reverse1(str1, 0))

main()
