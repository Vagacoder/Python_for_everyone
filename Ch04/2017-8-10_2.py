## Ch04 P4.17

n = int(input('Please enter an integer: '))


for i in range(2, n):
    count = 0
    for j in range(2,i):
        if i%j == 0:
            count += 1
    if count == 0:
        print(i)

