## P4.27
from random import *
from math import *

trials = 1000000
hit = 0

for i in range(trials):
    y_low = randint(0,2)
    alpha = randint(0,180)
    y_high = y_low + sin(radians(alpha))

    if y_high >= 2:
        hit += 1

print('Try/Hit = %.10f' %(trials/hit))

#P4.31

TOTAL_TICKET_NUM = 100
MAX_TICKET_PER_BUYER = 4

ticket_num = TOTAL_TICKET_NUM
buyer_num = 0

while ticket_num > 0:
    print('There are %d ticket(s) left.' %ticket_num)
    buy_num = input('How many ticket do you want ot buy (max 4 tickets per buyer): ')
    while buy_num == '' or int(buy_num) < 1 or int(buy_num) > MAX_TICKET_PER_BUYER or  ticket_num - int(buy_num) < 0:
        if buy_num == '' or (int(buy_num) < 1) or (int(buy_num) > MAX_TICKET_PER_BUYER) :
            buy_num = input('How many ticket do you want ot buy (max 4 tickets per buyer): ')
        elif ticket_num - int(buy_num) < 0 :
            buy_num = input('Not enough tickets left. '
                            '\nHow many ticket do you want ot buy (max 4 tickets per buyer): ')

    buy_num1 = int(buy_num)

    ticket_num -= buy_num1
    buyer_num += 1

print('Total buyer number is %d.' %buyer_num)

## P4.32

MAX_CAP = 100

total_ppl = 0

while total_ppl < MAX_CAP and total_ppl >= 0:
    ppl_input = input('Please enter the number of people come (negative for leaving): ')
    while total_ppl + int(ppl_input) > 100:
        print('Not enough space. Please try later')
        ppl_input = input('Please enter the number of people come (negative for leaving): ')
    ppl_coming = int(ppl_input)
    total_ppl += ppl_coming
    print('Currently, there are %d people inside.'%total_ppl)

print('Bar is full.')
