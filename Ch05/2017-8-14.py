## Ch05 R5.7

## translate phone# with letter to regular phone#(all are numbers)
# @para original_num is phone# with letter
# @return phone_num is all number.
phone_num = ''

def translatePhoneNum(original_num):
    phone_num = ''
    for i in original_num:
        if i.isdigit():
            phone_num += i
        elif i in '-()':
            phone_num += i
        elif i in 'AaBbCc':
            phone_num += '2'
        elif i in 'DdEeFf':
            phone_num += '3'
        elif i in 'GgHhIi':
            phone_num += '4'
        elif i in 'JjKkLl':
            phone_num += '5'
        elif i in 'MmNnOo':
            phone_num += '6'
        elif i in 'PpQqRrSs':
            phone_num += '7'
        elif i in 'TtUuVv':
            phone_num += '8'
        elif i in 'WwXxYyZz':
            phone_num += '9'
    return phone_num

print(translatePhoneNum('1-800-flowers'))



## Ch05 P5.21  improving P3.28

def romanDigit(number, small, middle, large):
    if number <= 3 and number >= 0:
        R_digit = small * number
    elif number == 4:
        R_digit = small + middle
    elif number >= 5 and number <= 8:
        R_digit = middle + small * (number - 5)
    elif number == 9:
        R_digit = small + large

    return R_digit

num = int(input('please enter an integer (1-3999): '))

if num > 3999 or num < 1:
    exit('Wrong input, please try again.')

one = num%10
ten = num//10%10
hun = num//100%10
thou = num//1000%10

print(thou, hun, ten, one)

r_thou = romanDigit(thou, 'M', '', '')
r_hun = romanDigit(hun, 'C', 'D', 'M')
r_ten = romanDigit(ten, 'X', 'L', 'C')
r_one = romanDigit(one, 'I', 'V', 'X')

print('The Roman number of %d is %s' %(num, r_thou + r_hun + r_ten + r_one))