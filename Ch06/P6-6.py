##Ch06 P6.6

values = [4, 8, 9, 7, 9, 6, 2, 10, 4, 8]

sum = 0
min = values[0]
for i in values:
    sum= sum + i
    if i < min:
        min = i

print(sum)
print(sum-min)
