## Ch08 P8.3

inFile = open('alice30.txt', 'r')

line = inFile.readline()
wordCount = dict()

while line != '':
    words = line.split()
    for word in words:
        word = word.strip()
        word = word.strip('.,!?;')
        newWord = ''
        
        for char in word:
            if char.isalpha():
                newWord += char
        
        newWord = newWord.lower()
        
        if newWord !='':
            if newWord not in wordCount:
                wordCount[newWord] = 1
            else:
                wordCount[newWord] +=1
    
    line = inFile.readline()

inFile.close()

countList = sorted(wordCount.values())
#print(countList)
top100Count = []

for i in range(1,101):
    top100Count.append(countList[-i])

#print(top100Count)

top100Words = []
for key in wordCount:
    if wordCount[key] in top100Count:
        top100Words.append(key)

print(top100Words)


