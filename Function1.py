## Test whether a string is palindrome (exp. 'RotoR')
# @para string, input string
# @return, Yes(True) or no(False) for palindrome

def isPalindrome(string):
    if len(string) <=1: return True
    print(string)
    if string[0] != string[len(string)-1]:
        test = False
    else:
        test = True

    return test and isPalindrome(string[1:len(string)-1])

## Test whether input number is an integer.
# @para number, input number for check
# @return, Yes(True) or no(False) for integer

def isInteger(number):
    if number < 10:
        if len(str(number//10)) == 1:
            return True
        else:
            return False
    else:
        return isInteger(number%10)


## Test prime number
# @para a, input number
# @return , Yes(True) or no(False) for prime number

def TestPrime(a):
    count = 0
    result = False

    for i in range(1, a + 1):
        if a % i == 0:
            count += 1
    if count == 2:
        result = True

    return result


##These two functions combined to find all sub-strings of the given string.
## subString_firstLetter alone can find all sub-string starting with first letter
# @para string , input string
# @return , sub-strings, sorting by letter order, then by the length of sub-string

def subString_firstLetter(string):
    if len(string) == 0: return
#    n = len(string)
#    print(n)
    print(string)
#    string = string[0:n-1]
    string = subString_firstLetter(string[0:len(string)-1])
    return


def All_subString(string):
    if len(string) == 0: return print('*')
    subString_firstLetter(string)
    All_subString(string[1:])
    return
