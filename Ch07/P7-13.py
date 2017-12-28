##Ch07 P7.13

sum = 0
inputString = input('Please input an float number: ')
count = 1
while inputString != 'Q' and inputString != 'q' and count < 2:
    try:
        number = float(inputString)
        count = 1
        sum += number

    except ValueError:
        print('Wrong input, please try again')
        count += 1

    inputString = input('Please input an float number: ')

print(sum)