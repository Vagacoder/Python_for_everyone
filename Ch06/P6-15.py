## CH06 P6.15

from random import *

list = []

for i in range(20):
    number = randint(1,6)
    list.append(number)

print(list)

maxRunNumber = list[0]
maxRunCount = 0
runCount = 0
for i in range(1,len(list)):

    if list[i] == list[i-1]:
        runNumber = list[i]
        runCount += 1
        if runCount > maxRunCount:
            maxRunCount = runCount
            maxRunNumber = runNumber
        
    elif list[i] != list[i-1]:
        runNumber = 0
        runCount = 0
        

string1=''
for i in list:
    string1 += str(i)

for i in range(len(string1)):
    if i == string1.index(str(maxRunNumber)*(maxRunCount+1)):
        print("("+string1[i], end ="")
    elif i == string1.index(str(maxRunNumber)*(maxRunCount+1))+maxRunCount:
        print(string1[i]+")", end ="")
    else:
        print (string1[i], end="")



