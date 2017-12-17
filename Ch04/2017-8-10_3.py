## P4.16

n = int(input('Please enter an integer: '))
#============ This is solution for P4.16

m = n
for i in range(1,n):
    while m%i == 0 and i != 1:
        m = m/i
        print(i)

print()

#============== NOT for P4.16, this is finding all factors.
count = 1

while count <= n/2:
    if n%count == 0 and count != 1:
        print(count)
    count +=1

print()

for i in range(1, n):
    if n%i == 0 and i != 1 and i != n:
        print(i)

print()
