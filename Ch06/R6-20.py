## Ch06 R6.20

values = [1, 2, 5, 5, 3, 1, 2, 4, 3, 2, 2, 2, 2, 3, 6, 5, 5, 6, 3, 1]

maxRunNumber = values[0]
maxRunCount = 0
runCount = 0
for i in range(1,len(values)):

    if values[i] == values[i-1]:
        runNumber = values[i]
        runCount += 1
        if runCount > maxRunCount:
            maxRunCount = runCount
            maxRunNumber = runNumber
        print("i is: %d" %i)
        print("runNumber is: %d" %runNumber)
        print("runCount is: %d" %runCount)
        print("maxRunNumber is: %d" %maxRunNumber)
        print("maxRunCount is: %d" %maxRunCount)
        
        
    elif values[i] != values[i-1]:
        runNumber = 0
        runCount = 0
        

print (maxRunNumber)
print (maxRunCount+1)
print("Number %d repeats for %d times." %(maxRunNumber, maxRunCount+1))


    
