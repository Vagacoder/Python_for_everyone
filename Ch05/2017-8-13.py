## Ch05 P5.5

def repeat(string, n, delim):
    new_string = string + (delim+string)*2
    return new_string

print(repeat('ho', 3, ', '))

## Ch05 P5.22

def balance(initial, rate, year):
    account_balance = initial * (1 + rate/100)**year
    return account_balance

print(balance(1000, 5, 1))

## Ch05 R5.6

def value(currency, float_number):
    print('%s%.2f'%(currency, float_number))

value('USD', 2985.39755)

## Ch05 P5.25

def printDigit(d):
    if d == 0 : print('||:::',end='')
    elif d == 1 : print(':::||',end='')
    elif d == 2 : print('::|:|',end='')
    elif d == 3 : print('::||:',end='')
    elif d == 4 : print(':|::|',end='')
    elif d == 5 : print(':|:|:',end='')
    elif d == 6 : print(':||::',end='')
    elif d == 7 : print('|:::|',end='')
    elif d == 8 : print('|::|:',end='')
    elif d == 9 : print('|:|::',end='')

def printZip(zipcode):
    zip_code = str(zipcode)
    print('|', end ='')
    sum = 0
    for i in zip_code:
        printDigit(int(i))
        sum += int(i)
    check = 10 - sum%10
    printDigit(check)
    print('|')

printZip(95014)
