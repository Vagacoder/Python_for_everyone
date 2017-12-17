## Ch05 P 5.27

def read_single_roman_number(n):
    if n == 'I': return 1
    if n == 'V': return 5
    if n == 'X': return 10
    if n == 'L': return 50
    if n == 'C': return 100
    if n == 'D': return 500
    if n == 'M': return 1000
    return 0

def read_roman_number(number):
    total = 0
    while len(number) > 1:
        first = read_single_roman_number(number[0])
        second = read_single_roman_number(number[1])
        if first >= second:
            total += first
            number = number[1:]
        else:
            total += (second - first)
            number = number[2:]
    total += read_single_roman_number(number)
    return total

print(read_roman_number('MDCCCXLVI'))

## Ch05 P 5.28

def input_financial_state():
    income = float(input('Please enter your family income (Enter -1 to stop): '))
    if income == -1:
        return
    children = int(input('Please enter the number of children (Enter -1 to stop): '))
    while income > 0 and children > 0:
        amount = calculate_financial_aid(income, children)
        print('You financial assistance is $%.2f.' %amount)
        income = float(input('Please enter your family income (Enter -1 to stop): '))
        if income == -1:
            return
        children = int(input('Please enter the number of children (Enter -1 to stop): '))


def calculate_financial_aid(income, children):
    if income <= 40000 and income > 30000 and children >=3:
        amount = 1000 * children
    elif income <= 30000 and income > 20000 and children >=2:
        amount = 1500 * children
    elif income < 20000:
        amount = 2000 * children
    else:
        amount = 0
    return amount

input_financial_state()

## Ch05 P 5.29
# Not perfect, miss the original user. Final result need +1


def reachablePeople(degree, averageFriends):
    if degree == 1:
        return averageFriends
    return reachablePeople(degree-1, averageFriends) * averageFriends + averageFriends


print(reachablePeople(4,2))


## Ch05 P 5.30

def password_Check():
    good_pw = False
    lower_count = False
    upper_count = False
    digit_count = False
    while not good_pw:
        pass_word = input('Please enter the password: ')
        for i in pass_word:
            if i.isupper():
                upper_count = True
            if i.islower():
                lower_count = True
            if i.isdigit():
                digit_count = True
        if len(pass_word) >= 8 and lower_count and upper_count and digit_count :
            good_pw = True


    return pass_word

print(password_Check())

