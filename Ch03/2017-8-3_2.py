## Ch03 P3.25

SINGLE_CAP1 = 8000
SINGLE_CAP2 = 32000

MARRY_CAP1 = 16000
MARRY_CAP2 = 64000

RATE1 = 0.1
RATE2 = 0.15
RATE3 = 0.25

base_tax = 0
taxing_amount = 0

state = input('Please enter S for single, M for married: ').upper()
income = int(input('Please enter your income in dollar: '))

if state == 'S':
    if income <= SINGLE_CAP1:
        tax_rate = RATE1

    elif income <= SINGLE_CAP2:
        base_tax = 800
        taxing_amount = SINGLE_CAP1
        tax_rate = RATE2

    elif income > SINGLE_CAP2:
        base_tax = 4400
        taxing_amount = SINGLE_CAP2
        tax_rate = RATE3

if state == 'M':
    if income <= MARRY_CAP1:
        tax_rate = RATE1

    elif income <= MARRY_CAP2:
        base_tax = 1600
        taxing_amount = MARRY_CAP1
        tax_rate = RATE2

    elif income > MARRY_CAP2:
        base_tax = 8800
        taxing_amount = MARRY_CAP2
        tax_rate = RATE3

print('Your tax is $%d.' %(base_tax + (income - taxing_amount) * tax_rate))
