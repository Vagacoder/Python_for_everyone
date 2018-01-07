## Ch08 P8.2

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

outFile = open('aliceCount.txt', 'w')
for key in sorted(wordCount):
    outFile.write(key + ': ' + str(wordCount[key]) + '\n')

outFile.close()
