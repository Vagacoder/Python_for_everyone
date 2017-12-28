## Ch07 P7.27

# process first file
inFile = open('nameandphone.txt', 'r')

nameList = []
phoneList = []
ssnList = []
incomeList = []

line = inFile.readline()

while line != '':

    data = line.rsplit(' ', 1)
    #print(data)
    nameList.append(data[0].strip())
    phoneList.append(data[1].strip())
    line = inFile.readline()

inFile.close()
#print(nameList)
#print(phoneList)

# process second file

inFile = open('nameandssn.txt', 'r')
line = inFile.readline()
lengthOfList = max(len(nameList), len(phoneList))
ssnList = [''] * lengthOfList

while line != '':

    data = line.rsplit(' ', 1)
    name = data[0].strip()
    ssn = data[1].strip()

    if name in nameList:
        index = nameList.index(name)
        ssnList[index] = ssn
    else:
        nameList.append(name)
        phoneList.append('')
        ssnList.append(ssn)

    line = inFile.readline()

inFile.close()
#print(nameList)
#print(phoneList)
#print(ssnList)

# procss third file

inFile = open('ssnandincome.txt', 'r')
line = inFile.readline()
lengthOfList = max(len(nameList), len(phoneList), len(ssnList))
incomeList = [''] * lengthOfList

while line != '':

    data = line.rsplit(' ', 1)
    ssn = data[0].strip()
    income = data[1].strip()

    if ssn in ssnList:
        index = ssnList.index(ssn)
        incomeList[index] = income
    else:
        nameList.append('')
        phoneList.append('')
        ssnList.append(ssn)
        incomeList.append(income)
    line = inFile.readline()

inFile.close()
print(nameList)
print(phoneList)
print(ssnList)
print(incomeList)