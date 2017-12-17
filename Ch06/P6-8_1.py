##Ch06 P6.8

values = [1, 4, 9, 16, 9, 7, 4, 9, 11]

sum = 0
for i in range(len(values)):
    if i%2 ==1:
        sum -=values[i]
    elif i%2 ==0:
        sum +=values[i]

print(sum)
