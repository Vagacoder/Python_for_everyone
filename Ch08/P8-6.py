## Ch08 P8.6

def main():
    inFile = open('p8-9.py', 'r')

    line = inFile.readline()
    lineIndex = 1
    
    idList = {}
    
    while line != '':
        ids = findIdentifier(line)
        
        for item in ids:
            if item in idList:
                idList[item].append(lineIndex)
            else:
                idList[item] = [lineIndex]
        
        line = inFile.readline()
        lineIndex +=1

    printAll(idList)
    
def findIdentifier(inputLine):
    itemList = inputLine.split()
    outputIdSet = set()
    
    for item in itemList:
        if checkId(item):
            outputIdSet.add(item)
                
    return outputIdSet

def checkId(inputString):
    isId = True
    
    if inputString[0].isalpha():
        for char in inputString:
            if not (char.isalpha() or char.isdigit() or char == '_'):
                isId = False
                break
    else:
        isId = False
    
    return isId
    

def printAll(inputDict):
    
    for item in sorted(inputDict):
        print(item, inputDict[item])

main()
