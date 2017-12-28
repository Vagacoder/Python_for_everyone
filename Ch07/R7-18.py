##Ch07 R7.18
str1= "a"
try:
    try:
        print(1/0)

    except ZeroDivisionError:
        print('Zero division')

    finally:
        print(str1[1])

except IndexError:
    print('Out of range')
