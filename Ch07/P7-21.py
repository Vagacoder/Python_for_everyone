## Ch07 P7.21

allLetter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
freq = [0]*26
inFile = open('out1.txt', 'r')

for line in inFile:

    for char in line:
        char = char.upper()
        if char in allLetter:
            index = allLetter.index(char)
        freq[index] += 1

inFile.close()

print(freq)