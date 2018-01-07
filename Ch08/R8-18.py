## Ch08 R8.18

gradeCounts = {'A': 8, 'D':3, 'B':15, 'F':2, 'C':6}

for key in gradeCounts:
    print(key)
    print(gradeCounts[key])
    print(key, gradeCounts[key])
    print()

for key in sorted(gradeCounts):
    print(key, gradeCounts[key])

sum = 0
number = len(gradeCounts)
for val in gradeCounts.values():
    sum += val
print(sum)
print('%.2f' % (sum/number))

print()

for key in sorted(gradeCounts):
    print(key+':', '*'*gradeCounts[key])