from random import *

a = [1,2,3,4,5]

def fillWithRandomNumbers(values) :

    number = []
    for i in range(len(values)) :
        number.append(random())

    print(number)
    values[:] = number
        
print(a)

fillWithRandomNumbers(a)

print(a)
