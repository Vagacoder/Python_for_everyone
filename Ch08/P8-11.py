## Ch08 P8.11

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

for letter in sorted(wordDict):
    print(letter + ': ', wordDict[letter])
        