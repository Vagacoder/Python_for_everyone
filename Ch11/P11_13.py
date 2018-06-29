# # P11.13
# function returns all subsets of characters of a string


def subSets(inputString):
    resultList = list()
    if len(inputString) <= 0:
        resultList.append(inputString)
    else:
        shorterList = subSets(inputString[1:])
        for str in shorterList:
            resultList.append(str)
            resultList.append(inputString[0] + str)
    return resultList


def main():
    string1 = "rum"
    print(subSets(string1))


main()
