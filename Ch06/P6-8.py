from random import*

a = [1,4,9,16,9,7,4,9,11]

def alternatingSum(list):
    sum = 0
    for i in range(len(list)):
        if i% 2 == 0:
            sum +=list[i]
        else:
            sum -= list[i]
    return sum

print(a)
print(alternatingSum(a))
