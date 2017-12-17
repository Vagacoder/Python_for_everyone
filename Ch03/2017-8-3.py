## Ch03 P3.19

#letter = input('please enter a single alphabetic letter: ')

letter = 'a'

if not letter.isalpha() or len(letter) > 1:
    exit('Wrong input, please try again.')

letter1 = letter.upper()

if letter1 == 'A' or letter1 == 'E' or letter1 == 'I' or letter1 == 'O' or letter1 == 'U':
    print('This is vowel.')
else:
    print('This is consonant.')

## Ch03 P3.21

num1 = float(input('please enter an float number: '))
num2 = float(input('please enter another float number: '))

if round(abs(num1 - num2),4) <= 0.01:
    print('they are same up to two decimal place.')


else:
    print('they are different.')

print(abs(num1 - num2))