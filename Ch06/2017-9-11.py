## Ch06 SC27

a = [1, 5,-12,57,2,-7,84,-90,21]

positive = []
for i in a:
    if i > 0:
        positive.append(i)

print(positive)

for i in range(len(positive)):
    if i > 0:
        print(",", end =" ")
    print(positive[i], end ="")


