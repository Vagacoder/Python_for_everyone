## Ch04 P4.28 and P4.29

one_dollar_2_yen = float(input('Please enter today\'s price of one dollar in yen: '))

dollar = 0.1

while dollar > 0:
    dollar = float(input('please enter the number of dollar (enter 0 to finish): '))
    if dollar > 0:
        yen = dollar*one_dollar_2_yen
        print('Your dollar equals %.2f yen.' %yen)

# below is P4.29
print()

one_yen_2_dollar = 1/one_dollar_2_yen

yen = 0.1

while yen > 0:
    yen = float(input('please enter the number of yen (enter 0 to finish): '))
    if yen > 0:
        dollar = yen*one_yen_2_dollar
        print('Your yen equals %.2f dollar.' %dollar)
