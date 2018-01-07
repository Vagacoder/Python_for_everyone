## Ch08 P8.14

# =============================================================================
# define the function of replace
# =============================================================================
def replace(string1, string2, string3):
    startIndex = string2.index(string1)
    endIndex = startIndex + len(string1)
    newString = string3[:startIndex] + '*' * len(string1) + string3[endIndex:]
    if string1 in newString:
        newString = replace(string1, newString.lower(), newString)
    return newString

# =============================================================================
# main
# =============================================================================
badWords = {'sex', 'drugs', 'fuck', 'shit'}

inFile = open('badinput.txt', 'r')
outFile = open('censored.txt', 'w')

line = inFile.readline()

while line != '':
    lowerLine = line.lower()
    for badWord in badWords:
        if badWord in lowerLine:
            line = replace(badWord, lowerLine, line)
    
    outFile.write(line)
    line = inFile.readline()

inFile.close()
outFile.close()


    
    