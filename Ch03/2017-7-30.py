## Ch03 compare2

x = float(input('please enter 1st number: '))
y = float(input('please enter 2nd number: '))

if x == y:
    print ('They are same number.')

else:
    if x > y:
        print ('first number is larger.')
    else:
        print('second number is larger.')

    if -0.01 < x-y and x-y < 0.01:
        print('They are close to each other.')

    if x == y + 1 or x == y -1:
        print ('They are one apart.')

    if x > 0 and y >0 or x < 0 and y < 0:
        print('They have same sign.')
    else:
        print('They are different sign.')
