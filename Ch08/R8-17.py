## Ch08 R8.17

ALL_UPPER = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
ALL_LOWER = set('abcdefghijklmnopqrstuvwxyz')
str1 = 'Sometimes I don\'t like the person I\'ve become!'
str2 = 'Drifting high up in a Sky that never ends?'

upper1 = set()
lower1 = set()
upper2 = set()
lower2 = set()

for char in str1:
    if char.isupper():
        upper1.add(char)
    elif char.islower():
        lower1.add(char)

for char in str2:
    if char.isupper():
        upper2.add(char)
    elif char.islower():
        lower2.add(char)

print(upper1.intersection(upper2))
print(lower1.intersection(lower2))
print(ALL_UPPER.difference(upper1.union(upper2)))
print(ALL_LOWER.difference(lower1.union(lower2)))
print(set(str1).difference(ALL_UPPER.union(ALL_LOWER)).union(set(str2).difference(ALL_UPPER.union(ALL_LOWER))))