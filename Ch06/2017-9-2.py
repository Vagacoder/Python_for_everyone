## Ch06 R6.3

a = ['a','b','c','d','e','f']
#b = [] + a
#for i in range(len(a)):
#    b.append(a[i])
b = a[0:(len(a)-1)]
b.append(a[len(a)-1])
print(a)
print(b)
print(b.pop(2))
print(b)
print(a)

## Ch06 P6.2
a = []

while len(a) < 10:
    num = int(input("please enter number: "))
    if not num in a:
        a.append(num)
    else:
        print("number already in list, ")

print(a)

## Ch06 P6.3

a = []

for i in range(2,10001):
    a.append(i)

for j in range(2, 101):
    for i in a:
        if i !=j and i%j == 0:
            a.remove(i)

print(a)


## Ch06 SC18

names = ['a','b','c','d','e','f']
name = list(names)

# method1
for i in range(len(names)-1, -1, -1) :
    if names[i] == 'f' :
        names.pop(i)

print(names)

# method2
i = len(name)-1

while i >= 0:
    if name[i] == 'f':
        name.pop(i)

    i -= 1
print(name)