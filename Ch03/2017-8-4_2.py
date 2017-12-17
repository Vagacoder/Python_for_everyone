## Ch03 P3.33

PASS = '1234'

for i in range(3):
    #pass_word = input('Please enter your PIN number: ')
    pass_word = '123'
    if pass_word == PASS:
        print('Your PIN is correct.')
        exit()
    else:
        print('Your PIN is INCORRECT.')

print('Your card is blocked')

## Ch03 P3.35

cost = float(input('Please enter your cost in restaurant: '))
s_level = input('Please enter your satisfaction level, 1 = totally satisfied; 2= satisfied; 3 = dissatisfied: ')

TIP_RATE1 = 0.2
TIP_RATE2 = 0.15
TIP_RATE3 = 0.1

S_LVL1 = 'totally satisfied'
S_LVL2 = 'satisfied'
S_LVL3 = 'dissatisfied'

if s_level == '1':
    tip_rate = TIP_RATE1
    s_lvl = S_LVL1

elif s_level == '2':
    tip_rate = TIP_RATE2
    s_lvl = S_LVL2

elif s_level == '3':
    tip_rate = TIP_RATE3
    s_lvl = S_LVL3

print('You are %s with this dinner, and the tip is $%.2f.' %(s_lvl, cost * tip_rate))