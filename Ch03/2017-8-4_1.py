## Ch03 P3.31

save_ini = float(input('Please enter initial balance in saving account: '))
if save_ini < 0:
    exit('Wrong input, please try again.')

check_ini = float(input('Please enter initial balance in checking account: '))
if check_ini < 0:
    exit('Wrong input, please try again.')

mode = input('Please enter D for deposit, W for withdrawal or T for transfer: ').upper()
if mode != 'D' and mode != 'W' and mode != 'T':
    exit('Wrong input, please try again.')

account = input('Please choose account, C for checking; S for saving: ').upper()
if account != 'C' and account != 'S':
    exit('Wrong input, please try again.')

amount = float(input('Please enter the amount: '))
if amount < 0:
    exit('Wrong input, please try again.')
if mode == 'D':
    amount = -amount

save_balance = save_ini
check_balance = check_ini
cash = 0

if account == 'C':
    if amount > check_balance:
        exit('Not enough money in checking account.')

    check_balance -= amount

    if mode == 'T':
        save_balance += amount
    elif mode == 'W':
        cash = amount

if account == 'S':
    if amount > save_balance:
        exit('Not enough money in saving account.')

    save_balance -= amount

    if mode == 'T':
        check_balance += amount
    elif mode == 'W':
        cash = amount

print('Saving balance is $%.2f' %(save_balance))
print('Checking balance is $%.2f'%(check_balance))
print('You reiceve cash $%.2f' %(cash))