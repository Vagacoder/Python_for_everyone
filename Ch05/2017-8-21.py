## Ch05 P 5.14

## convert time format (hour, minute) in number to word.
# @para hour, input hour 1-12 format
# @para minute, input minute 0-59 format
# @return , time in English name

def getTimeName(hour, minute):
    hourName = getHour(hour)
    minuteName = getMinute(minute)

    if minute == 0:
        timeName = hourName + ' o\'clock'

    elif minute <= 30:
        timeName = minuteName + ' pass ' + hourName

    elif minute < 60:
        hourName = getHour(hour + 1)
        timeName = minuteName + ' to ' + hourName

    return timeName


def getHour(number):
    if number == 1: return "one"
    if number == 2: return "two"
    if number == 3: return "three"
    if number == 4: return "four"
    if number == 5: return "five"
    if number == 6: return "six"
    if number == 7: return "seven"
    if number == 8: return "eight"
    if number == 9: return "nine"
    if number == 10: return "ten"
    if number == 11: return "eleven"
    if number == 12: return "twelve"
    return ""

def getMinute(number):
    if number < 20:
        minute = digitName(number)
    elif number < 30:
        minute = tensName(number) +' ' + digitName(number%10)
    elif number == 30:
        minute = 'half'
    elif number < 40:
        minute = tensName(60 - number) + ' ' + digitName((60 - number)%10)
    elif number == 40:
        minute = tensName(60 - number) + digitName((60 - number) % 10)
    elif number < 60:
        minute = digitName(60 - number)

    return minute


def digitName(number) :
    if number == 1 : return "one"
    if number == 2 : return "two"
    if number == 3 : return "three"
    if number == 4 : return "four"
    if number == 5 : return "five"
    if number == 6 : return "six"
    if number == 7 : return "seven"
    if number == 8 : return "eight"
    if number == 9 : return "nine"
    if number == 10 : return "ten"
    if number == 11 : return "eleven"
    if number == 12 : return "twelve"
    if number == 13 : return "thirteen"
    if number == 14 : return "fourteen"
    if number == 15 : return "a quarter"
    if number == 16 : return "sixteen"
    if number == 17 : return "seventeen"
    if number == 18 : return "eighteen"
    if number == 19 : return "nineteen"
    return ""

def tensName(number) :
    if number == 30 : return "thirty"
    if number >= 20 : return "twenty"
    return ""

print(getTimeName(9,57))


