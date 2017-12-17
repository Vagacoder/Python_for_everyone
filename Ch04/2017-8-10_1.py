## Ch04 P4.15

n = int(input('Please enter an integer: '))

f1 = 1
f2 = 1
count = 0

while count < n-2 :
    fn = f1 + f2
    f1 = f2
    f2 = fn
    count += 1

print('n is:', n, '  cycle number:', count, '  f%d is'%(n),fn)
