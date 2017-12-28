##CH07 P7.5

inputName = 'lyrics.txt'
inputFile = open(inputName, 'r')

lineNumber = 0
wordNumber = 0
charNumber = 0
for line in inputFile:
    if line != '':
        lineNumber +=1
        line = line.strip()
        words = line.split()
        wordNumber += len(words)
        for word in words:
            charNumber += len(word)

print('The number of lines is: %d' %lineNumber)
print('The number of words is: %d' %wordNumber)
print('The number of character is: %d' %charNumber)