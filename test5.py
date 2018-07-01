# -*- coding: utf-8 -*-

## testing operator << and >>
print(3)
print(7 << 1)
print(7 >> 1)
print()

a = "Here is + a = test question."
b = a.replace("e", "1")
print(b)

c = [""]*10
c[3] = 10
print(c)

d = {0:'s', 1:'e', 2:'n', 3:'d', 4:'m', 5:'o', 6:'r', 7:'y', 8:'', 9:''}
print(sorted(d))
print(d.values())
print('abc' + '*'*10)
print('abc'.isalpha())
print('abc'.index('c'))