## Ch05 P 5.15

def reverse(string):
    if string == "":
        return string
    else:
        return reverse(string[1:]) + string[0]

print(reverse('flow'))

## Ch05 P 5.16

def isPalindrome(string):
    if len(string) <2:
        return True
    if string[0] == string[-1]:
        test = True
    else:
        test = False
    return isPalindrome(string[1:-1]) and test

print(isPalindrome('rt'))

## Ch05 P 5.17

def find(string1, string2):
    if len(string1) < len(string2):
        return False
    if string1[0:len(string2)] == string2:
        test = True
    else:
        test = False
    return find(string1[1:], string2) or test

print(find('Missipssppi', 'sip'))

## Ch05 P 5.19

def exponential(a, n):
    if n == 1:
        return a
    return a * exponential(a, n-1)

print(exponential(3,3))

## Ch05 P 5.20
def leap_year():
    year = int(input('please enter the year: '))

    if year%4 == 0:
        if year%400 == 0:
            return 'is a leap year.'
        elif year%100 == 0:
            return 'is NOT a leap year.'
        else:
            return 'is a leap year.'

    else:
        return 'is NOT a leap year.'

print(leap_year())
