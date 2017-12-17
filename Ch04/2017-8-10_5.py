## P4.23
from random import *

INI_size = randint(10,100)
print('Initial size is %d.'%INI_size)
n = INI_size

starter = randint(0,1)
#starter = 1
if starter == 0:
    print('Computer takes first turn.')
elif starter == 1:
    print('You take first turn.')

Com_model = randint(0,1)
#Com_model = 0
if Com_model == 0:
    print('Computer is in smart model.')
elif Com_model == 1:
    print('Computer is in stupid model.')

turn = 0

if starter == 0:
    while n > 1:
        if Com_model == 0:
            if n > 63:
                Com_take = n - 63
                if Com_take > n//2:
                    Com_take = randint(1, n//2)
            elif n > 31:
                Com_take = n - 31
                if Com_take > n//2:
                    Com_take = randint(1, n//2)
            elif n > 15:
                Com_take = n - 15
                if Com_take > n//2:
                    Com_take = randint(1, n//2)
            elif n > 7:
                Com_take = n - 7
                if Com_take > n//2:
                    Com_take = randint(1, n//2)
            elif n > 3:
                Com_take = n - 3
                if Com_take > n//2:
                    Com_take = randint(1, n//2)
            elif n > 1:
                Com_take = n - 1
                if Com_take > n//2:
                    Com_take = randint(1, n//2)

        elif Com_model == 1:
            Com_take = randint(1, n//2)


        n = n - Com_take
        print('Computer takes %d, %d remained.' %(Com_take, n))

        turn += 1

        if n <= 1:
            break

        you_take = input('please enter number you take: ')
        while not you_take.isdigit() or int(you_take) > n/2:
            you_take = input('please enter number you take: ')
        you_take = int(you_take)

        n = n - you_take
        print('You take %d, %d remained.' %(you_take, n))

        turn += 1

    if turn%2 == 1:
        print('Computer wins!')
    elif turn%2 == 0:
        print('You win!')


if starter == 1:
    while n > 1:
        you_take = input('please enter number you take: ')
        while not you_take.isdigit() or int(you_take) > n/2:
            you_take = input('please enter number you take: ')
        you_take = int(you_take)

        n = n - you_take
        print('You take %d, %d remained.' %(you_take, n))

        turn += 1

        if n <= 1:
            break

        if Com_model == 0:
            if n > 63:
                Com_take = n - 63
                if Com_take > n//2:
                    Com_take = randint(1, n//2)
            elif n > 31:
                Com_take = n - 31
                if Com_take > n//2:
                    Com_take = randint(1, n//2)
            elif n > 15:
                Com_take = n - 15
                if Com_take > n//2:
                    Com_take = randint(1, n//2)
            elif n > 7:
                Com_take = n - 7
                if Com_take > n//2:
                    Com_take = randint(1, n//2)
            elif n > 3:
                Com_take = n - 3
                if Com_take > n//2:
                    Com_take = randint(1, n//2)
            elif n > 1:
                Com_take = n - 1
                if Com_take > n//2:
                    Com_take = randint(1, n//2)

        elif Com_model == 1:
            Com_take = randint(1, n//2)


        n = n - Com_take
        print('Computer takes %d, %d remained.' %(Com_take, n))

        turn += 1

    if turn%2 == 1:
        print('You wins')
    elif turn%2 == 0:
        print('Computer wins!')




