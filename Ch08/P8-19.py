## Ch08 P8.19

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

userIn = input('Please enter word (enter Q for finish): ')
while userIn != 'Q':
    if userIn in wordCount:
        print(wordCount[userIn])
    else:
        print('Not found!')
    userIn = input('Please enter word (enter Q for finish): ')
    
