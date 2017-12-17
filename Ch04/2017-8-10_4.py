## Ch04 P4.18

for i in range(1,11):
    for j in range(1,11):
        print('%4d'%(i*j), end=' ')
    print()

## CH04 P4.21
n = input('please enter an integer (>=3): ')

while not n.isdigit() or int(n) <3:
    n = input('please enter an integer (>=3): ')
n = int(n)

for i in range(n):
    if i == 0 or i == n-1:
        print('*'*n, '*'*n)
    else:
        print('*'*n, '*%s*'%(' '*(n-2)))


