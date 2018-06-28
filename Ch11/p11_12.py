# # P11_12
# function returns all substrings of one string


# Solution 1, including 2 methods
# recursive subString method
def subString(inputString):
    listOfSubString = list()
    if len(inputString) <= 0:
        listOfSubString.append(inputString)

    else:
        listOfSubString = subStringOfFirstLetter(inputString)
        returnedList = subString(inputString[1:])
        for str1 in returnedList:
            listOfSubString.append(str1)

    return listOfSubString


# help method
def subStringOfFirstLetter(inputString):
    listOfSubString = list()

    for i in range(1, len(inputString)+1):
        listOfSubString.append(inputString[:i])

    return listOfSubString


## Solution 2, try to use one method
# recursive subString method
def subString1(inputString):
    listOfSubString = list()
    if len(inputString) <= 0:
        listOfSubString.append(inputString)

    else:
        for i in range(1, len(inputString) + 1):
            listOfSubString.append(inputString[:i])
        returnedList = subString(inputString[1:])
        for str1 in returnedList:
            listOfSubString.append(str1)

    return listOfSubString


# main method
def main():
    string1 = "rum"
    print(string1[:0])
    print(string1[:1])
    print(string1[:2])
    print(string1[:3])
    print(subString(string1))
    print(subString1(string1))


main()
