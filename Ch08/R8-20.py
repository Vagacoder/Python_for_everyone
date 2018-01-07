## Ch08 R8.20

set1 = {1,2,3,4,5,8}
set2 = {2,3,5,6,7,9}
set3 = {1,3,4,7,9,10}

setA = set1.union(set2).difference(set1.intersection(set2))
print(setA)
setB = set1.difference(set2.union(set3)).union(set2.difference(set1.union(set3))).union(set3.difference(set1.union(set2)))
print(setB)
setC = set1.union(set2)
print(setC)

setD = set()

for i in range(1, 26):
    if i not in set1:
        setD.add(i)

print(setD)

setE = set()

for i in range(1, 26):
    if i not in set1.union(set2).union(set3):
        setE.add(i)

print(setE)

setF = set()

for i in range(1, 26):
    if i not in set1.intersection(set2).intersection(set3):
        setF.add(i)

print(setF)