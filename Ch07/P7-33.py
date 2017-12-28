## Ch07 P7.33

from math import *

inFile = open('rc.txt', 'r')

line = inFile.readline()
line = inFile.readline()

timeList = []
voltageList = []

while line != '':
    data = line.split(':')
    time = int(data[0].strip())
    voltage = float(data[1].strip())
    timeList.append(time)
    voltageList.append(voltage)
    line = inFile.readline()
    
#print(timeList)
#print(voltageList)

B = voltageList[-1]
startB = B * 0.05
endB = B * 0.95
print(startB)
print(endB)

startVol = voltageList[0]
endVol = voltageList[0]

for i in range(len(voltageList)):
    voltage = voltageList[i]
    if abs(voltage - startB) < abs(startVol - startB):
        startVol = voltage
    if abs(voltage - endB) < abs(endVol - endB):
        endVol = voltage

inFile.close()

startIndex = voltageList.index(startVol)
startTime = timeList[startIndex]

endIndex = voltageList.index(endVol)
endTime = timeList[endIndex]

print(startVol)
print(endVol)

print('Start time is %d, end time is %d' %(startTime, endTime))
