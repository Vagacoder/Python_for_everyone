## Ch05 P 5.26

def read_digit(code):
    bar1 = read_bar(code[0])
    bar2 = read_bar(code[1])
    bar3 = read_bar(code[2])
    bar4 = read_bar(code[3])
    bar5 = read_bar(code[4])
    number = bar1 * 7 + bar2 * 4 + bar3 * 2 + bar4 * 1 + bar5 * 0
    if number == 11:
        number = 0
    return number


def read_bar(bar):
    if bar == '|':return 1
    elif bar == ':':return 0

def read_zipcode(zip):
    if len(zip) != 32 or zip[0] != '|' or zip[-1] != '|':
        return 'Wrong bar code!'

    digit1 = read_digit(zip[1:6])
    digit2 = read_digit(zip[6:11])
    digit3 = read_digit(zip[11:16])
    digit4 = read_digit(zip[16:21])
    digit5 = read_digit(zip[21:26])
    check = read_digit(zip[26:31])

    sum = digit1+digit2+digit3+digit4+digit5


    if (sum + check) %10 != 0:
        return 'Wrong check bar code!'
    else:
        return str(digit1) + str(digit2) + str(digit3) + str(digit4) + str(digit5)

print(read_zipcode('||:|::::||::::||||::::|:|:::|:||'))