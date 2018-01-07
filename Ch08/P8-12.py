## Ch08 P8.12


# =============================================================================
# set arguments
# =============================================================================
ALL_LETTER = 'abcdefghijklmnopqrstuvwxyz'

# =============================================================================
# read file and process words in this file, add words to a set
# =============================================================================
inFile = open('..\ch07\lyrics.txt','r')
wordSet= set()

for line in inFile:
    words = line.strip().lower().split()
    for word in words:
        word = word.strip('.,!?;\'\"')
        if word.isalpha():
            wordSet.add(word)
        else:
            newWord = ''
            for char in word:
                if char.isalpha():
                    newWord += char
            wordSet.add(newWord)

#print(wordSet)

# =============================================================================
# setup  a dictionary, keys are letters, values are empty sets.            
# =============================================================================
wordDict = {} 

for letter in ALL_LETTER:
    newSet = set()
    wordDict[letter] = newSet

#print(wordDict)

# =============================================================================
# add words into dictionary
# =============================================================================

for word in wordSet:
    for letter in word:
        wordDict[letter].add(word)
        
# =============================================================================
# Ask user input a word, and search dictionary to find any words containing all
# letters in input word.
# =============================================================================

userWord = input('Please enter a word: ')

resultWordSet = wordDict[userWord[0]]
for char in userWord:
    if char.isalpha():
        resultWordSet = resultWordSet.intersection(wordDict[char])

print(resultWordSet)
        
        
        
        