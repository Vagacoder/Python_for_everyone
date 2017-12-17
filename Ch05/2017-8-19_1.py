## Ch05 P5.16

def isPalindrome(string):
    if len(string) <=1: return True
    print(string)
    if string[0] != string[len(string)-1]:
        test = False
    else:
        test = True

    return test and isPalindrome(string[1:len(string)-1])

def main(string):
    print(isPalindrome(string))


main('aibberia')

## Ch05 P5.18

def isInteger(number):
    if number < 10:
        if len(str(number//10)) == 1:
            return True
        else:
            return False
    else:
        return isInteger(number%10)




def main(number):
    print(isInteger(number))

main(11.2)

## Ch05 R5.2h
# calculate the weekday of date
def weekDay(year, month, day):

    d = day
    print(d)
    m = shiftMonth(month)
    print(m)
    c = year // 100
    if month == 1 or month == 2:
        y = year%100 -1
    else:
        y = year%100
    if y < 0:
        y += 100
        c += -1

    print('y',y)

    print('c',c)


    w = ( d + int(2.6*m -0.2) + y + int(y/4) + int(c/4) - 2*c )%7
    print(int(2.6*m -0.2))
    print(int(y/4))
    print(int(c/4))
    print(w)

    while w < 0:
        w += 7

    if w == 0 : weekday = 'Sunday'
    elif w == 1 : weekday = 'Monday'
    elif w == 2 : weekday = 'Tuesday'
    elif w == 3 : weekday = 'Wedsday'
    elif w == 4 : weekday = 'Thursday'
    elif w == 5 : weekday = 'Friday'
    elif w == 6 : weekday = 'Saturday'

    return weekday


def shiftMonth(month):
    if month >= 3 and month <=12:
        month += -2
    elif month >= 1 and month <= 2 :
        month += 10

    return month

print(weekDay(2015, 2, 19))