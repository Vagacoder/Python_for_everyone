## Ch03 P3.28
num = int(input('please enter an integer (1-3999): '))

if num > 3999 or num < 1:
    exit('Wrong input, please try again.')

thou = num//1000
hun = (num - thou*1000)//100
ten = (num - thou*1000 - hun*100)//10
one = (num - thou*1000 - hun*100 - ten*10)

print(thou, hun, ten, one)

hun_C_front = 0
hun_D =0
hun_M = 0
hun_C_back = 0

if thou <= 3 and thou >= 0 :
    thou_M = thou

if hun <= 3 and hun > 0 :
    hun_C_front = hun
elif hun >3 and hun <9:
    hun_D = 1
    if hun == 4:
        hun_C_front = 1
    elif hun >= 5 and hun <9:
        hun_C_back = hun -5
elif hun == 9:
    hun_M = 1
    hun_C_front = 1

ten_X_front = 0
ten_L =0
ten_C = 0
ten_X_back = 0

if ten <= 3 and ten > 0 :
    ten_X_front = ten
elif ten >3 and ten <9:
    ten_L = 1
    if ten == 4:
        ten_X_front = 1
    elif ten >=5 and ten <9:
        ten_X_back = ten -5
elif ten == 9:
    ten_C = 1
    ten_X_front = 1

one_I_front = 0
one_V =0
one_X = 0
one_I_back = 0

if one <= 3 and one > 0 :
    one_I_front = one
elif one >3 and one <9:
    one_V = 1
    if one == 4:
        one_I_front = 1
    elif one >=5 and one <9:
        one_I_back = one -5
elif one == 9:
    one_X = 1
    one_I_front = 1

print('The Roman number of %d is ' %(num) + 'M'*thou_M + 'C'*hun_C_front + 'D'*hun_D  + 'M'*hun_M + \
      'C'*hun_C_back + 'X'*ten_X_front + 'L'*ten_L + 'C'*ten_C + 'X'*ten_X_back + 'I'*one_I_front + \
      'V'*one_V + 'X'*one_X + 'I'*one_I_back)


