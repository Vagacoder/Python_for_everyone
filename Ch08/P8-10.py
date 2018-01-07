## Ch08 P8.10

inFile1 = open('..\ch07\hello.txt', 'r')
inFile2 = open('..\ch07\hello1.txt', 'r')

set1 = set()
set2 = set()

for line in inFile1:
    
    words = line.strip().split()
    for word in words:
        word = word.strip('.,!?;\'\"')
        if word.isalpha():
            set1.add(word)
        else:
            newWord = ''
            for char in word:
                if char.isalpha():
                    newWord += char
            set1.add(newWord)


for line in inFile2:
    
    words = line.strip().split()
    for word in words:
        word = word.strip('.,!?;\'\"')
        if word.isalpha():
            set2.add(word)
        else:
            newWord = ''
            for char in word:
                if char.isalpha():
                    newWord += char
            set2.add(newWord)

inFile1.close()
inFile2.close()

print(set1)
print(set2)

print(sorted(set1.intersection(set2)))