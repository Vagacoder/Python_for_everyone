## Ch03 P3.27

year = int(input('please enter the year: '))

if year%4 == 0:
    if year%400 == 0:
        print(year, 'is a leap year.')
    elif year%100 == 0:
        print(year, 'is NOT a leap year.')
    else:
        print(year, 'is a leap year.')

else:
    print(year, 'is NOT a leap year.')

print()

#if year%4 == 0 or (year%400 == 0 and year%100 == 0):
#    print(year, 'is a leap year.')
#
#else:
#    print(year, 'is NOT a leap year.')
#
#print()

if year%4 != 0 or (year%100 == 0 and year%400 != 0):
    print(year, 'is NOT a leap year.')

else:
    print(year, 'is a leap year.')

print()

if year%4 == 0 and year%100 != 0 or year%400 == 0:
    print(year, 'is a leap year.')

else:
    print(year, 'is NOT a leap year.')