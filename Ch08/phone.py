## 

def main():
    myContacts = {"Fred": 7235591, "Mary": 3841212,
                  "Bob": 3841212, "Sarah": 2213278}

    if "Fred" in myContacts:
        print("Number for Fred:", myContacts["Fred"])
    else:
        print("Fred is not in my contact list.")

    nameList = findNames(myContacts, 3841212)
    print("Names for 384-1212: ", end="")
    for name in nameList:
        print(name, end=" ")
    print()
    printAll(myContacts)


def findNames(contacts, number):
    nameList = []
    for name in contacts:
        if contacts[name] == number:
            nameList.append(name)

    return nameList


def printAll(contacts):
    print("All names and numbers:")
    for key in sorted(contacts):
        number = str(contacts[key])
        number = number[0:3] + "-" + number[3:]
        print("%-10s %s" % (key, number))

main()
