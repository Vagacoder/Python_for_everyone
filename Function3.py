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