## Ch08 P8.9

str1 = 'We are students, we are here to study!'
str2 = 'We like reading books, we are doing some study on education.'
list1 = str1.split()
set1 = set()
for item in list1:
    item = item.strip('.,!?')
    set1.add(item)
print(set1)

list2 = str2.split()
set2 = set()
for item in list2:
    item = item.strip('.,!?')
    set2.add(item)
print(set2)


print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))

newSet1 = set(str1)
newSet1_1 = set()
newSet2 = set(str2)
newSet2_1 = set()
for i in newSet1:
    if i.isalpha(): 
        newSet1_1.add(i.lower())

print(newSet1_1)

for i in newSet2:
    if i.isalpha():
        newSet2_1.add(i.lower())

print(newSet2_1)

allAlpha = set('abcdefghijklmnopqrstuvwxyz')
print(newSet1_1.intersection(newSet2_1))
print(newSet1_1.difference(newSet2_1))
print(newSet2_1.difference(newSet1_1))
print(allAlpha.difference(newSet1_1.union(newSet2_1)))
