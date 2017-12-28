##Ch07 P7.7


def checkWord(rawInputWord):
    inputWord = rawInputWord.strip('.,;!?()').lower()
    found = False
    wordlist = open('words.txt', 'r')
    for line in wordlist:
        if inputWord in line:
            found = True
            break
    if not found:
        print(rawInputWord)


##
fileName = input('Please enter the name of file: ')

done = False
while not done :
    try:
        inFile = open(fileName, 'r')
        done = True

    except IOError:
        print('Wrong file name, try again!')

for line in inFile:
    words = line.split()
    for word in words:
        checkWord(word)

inFile.close()
