## Ch08 R8.16
ALL_LETTERS = 'abcdefghijklmnopqrestuvwxyz'
str1 = 'Think of me, when you see the sun or feel the wind!'

letterCount = {}
for char in str1:
    if char.isalpha():
        char = char.lower()
        if char in letterCount:
            letterCount[char] += 1
        else:
            letterCount[char] = 1

mostCommonLetter = sorted(letterCount)[0]
notPresentedLetter = set()

for key in letterCount:
    if letterCount[key] > letterCount[mostCommonLetter]:
        mostCommonLetter = key

for char in ALL_LETTERS:
    if char not in letterCount:
        notPresentedLetter.add(char)
        

print(mostCommonLetter)
print(notPresentedLetter)
print(letterCount)
           

