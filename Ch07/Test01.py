#from os import *

inFile = open("hello.txt", "rb")


print(inFile.tell())
inFile.seek(4)
print(inFile.tell())
content = inFile.read(3)
print(content)
print(inFile.tell())
inFile.seek(-4, 1)
print(inFile.tell())
content = inFile.read(1)
print(content)
inFile.close()

outputFile = open('hello.txt', 'a')
outputFile.write('\nwriting test')
outputFile.write('\nwriting test2')
outputFile.close()
