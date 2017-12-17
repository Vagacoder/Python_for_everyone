## Ch03 P3.5 & P3.6

a = int(input('Please enter first integer: '))
b = int(input('Please enter second integer: '))
c = int(input('Please enter third integer: '))
model = input('Please enter "strict" or "lenient": ')

if model == 'strict':

    if a < b and b < c :
        print('increasing')

    elif a > b and b > c :
        print('decreasing')

    else:
        print('neither')

if model == 'lenient':

    if a == b and b == c:
        print('both')

    elif a <= b and b <=c:
        print('increasing')

    elif a >= b and b >= c:
        print('decreasing')

    else:
        print('neither')

