## Ch05 sc29

## function calculate cube of 1 to n (input integer) and print a table
# @para number is an integer input
# @return a table of the cubes from 1**3 to n**3

def cubeTable(number):
    print('+-----+-----------+')
    print('|   i | i * i * i |')
    print('+-----+-----------+')
    for i in range(1,number+1):
        c_num = cube(i)
        print('|%4d |%10d |'%(i, c_num))
    print('+-----+-----------+')

## calculate cube of input
# @para n is input integer
# @return is cube of n

def cube(n):
    return n**3

cubeTable(100)
