## Ch08 P8.4

import numpy

n = 100

setOfNumber = set()

for i in range(1, n+1):
    setOfNumber.add(i)
print(setOfNumber)

setOfNoPrime =set()

for i in range(2, int(numpy.sqrt(n))+1):
    for j in setOfNumber:
        if j%i == 0 and j != i:
            setOfNoPrime.add(j)

print(setOfNoPrime)
print(setOfNumber.difference(setOfNoPrime))