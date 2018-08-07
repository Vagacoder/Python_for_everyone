## Dictionary

counts = {'chuck': 1, 'annie': 42, 'jan': 100}

# dic.get() return the value of key, if key does not exsist, return default value
print(counts.get('jan', 200))
print(counts.get('jack', 200))

word = 'brontosaurus'
d = dict()

for c in word:
    d[c] = d.get(c, 0) + 1

print(d)

print(d.keys())
print(list(d.keys()))
print(sorted(d.keys()))
