inFile = open('hello.txt', 'rb')
print(inFile.tell())

text = inFile.read(1)
print(len(text))
print(text)

print()

inFile.seek(2, 1)
print(inFile.tell())
t = inFile.read(1)
print(t)

print()

inFile.seek(1, 1)
print(inFile.tell())
t = inFile.read(1)
print(t)

print()

inFile.seek(100, 1)
print(inFile.tell())
t = inFile.read(1)
print(t)

