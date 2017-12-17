## Ch04 P4.12

a = 'abcd'

# sorting as requested
for i in range(1,len(a)+1):
    for j in range(0,len(a)-i):
        print(a[j:j+i])

print()
# sorting in a way easier to understand
for i in range(0, len(a)+1):
    for j in range(i+1, len(a)):
        print(a[i:j])

print('Q')