## Ch03 P3.14

#card = input('Please enter your card notation: ').upper()
card = 'QS'

if 'A' in card:
    number = 'Ace'
elif '2' in card:
    number = '2'
elif '3' in card:
    number = '3'
elif '4' in card:
    number = '4'
elif '5' in card:
    number = '5'
elif '6' in card:
    number = '6'
elif '7' in card:
    number = '7'
elif '8' in card:
    number = '8'
elif '9' in card:
    number = '9'
elif '10' in card:
    number = '10'
elif 'J' in card:
    number = 'Jack'
elif 'Q' in card:
    number = 'Queen'
elif 'K' in card:
    number = 'King'

if 'D' in card:
    color = 'Diamond'
elif 'H' in card:
    color = 'Hearts'
elif 'S' in card:
    color = 'Spades'
elif 'C' in card:
    color = 'Clubs'

print('%s of %s' %(number, color))

## Ch 03 P3.16

#str1 = input('first string: ')
#str2 = input('second string: ')
#str3 = input('third string: ')

str1 = 'able'
str2 = 'baker'
str3 = 'Charlie'

if str1 < str2 and str1 < str3:
    if str2 < str3:
        print(str1)
        print(str2)
        print(str3)
    elif str2 > str3:
        print(str1)
        print(str3)
        print(str2)

elif str2 < str1 and str2 < str3:
    if str1 < str3:
        print(str2)
        print(str1)
        print(str3)
    elif str1 > str3:
        print(str2)
        print(str3)
        print(str1)

elif str3 < str1 and str3 < str2:
    if str1 < str2:
        print(str3)
        print(str1)
        print(str2)
    elif str1 > str2:
        print(str3)
        print(str2)
        print(str1)

## Ch03 P3.17

string = input('please enter a string: ')

if string.isalpha():
    print('only letters')

if string.isupper() and string.isalpha():
    print ('only upper letters')

if string.islower() and string.isalpha():
    print('only lower letters')

if string.isdigit():
    print('only digits')

if string.isalnum():
    print('only letter and number')

if string[0].isupper():
    print('start with upper letter')

if string.endswith('.'):
    print('ends with period')