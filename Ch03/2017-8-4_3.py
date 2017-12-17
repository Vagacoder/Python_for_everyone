## Ch03 3.39

code_ini = input('please enter control code: ')
if len(code_ini) != 9:
    exit('wrong')

code = code_ini
L_door =''
R_door =''

if code[3] == '1' and code[8] =='P':
    if code[0] == '1' or code[5] == '1':
        L_door = 'open'
    if code[1] == '1' or code[7] == '1':
        R_door = 'open'
    if code[2] == '0':
        if code[4] == '1':
            L_door = 'open'
        if code[6] == '1':
            R_door = 'open'

#else:
#    L_door = 'close'
#    R_door = 'close'
if L_door == 'open':
    print('Left door is open.')
if R_door == 'open':
    print('Right door is open.')

if L_door != 'open' and R_door != 'open':
    print('Both doors are closed.')