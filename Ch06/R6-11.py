##Ch06 R6.11

values = []

valuesNumber =10
count = 0

while count < valuesNumber :
    inputNumber = int(input("Please enter a number: "))
    count +=1
    values.append(inputNumber)

print(values)
    
valuesLength = len(values)

for i in range(valuesLength-1, -1, -1):
    print(values[i])


    
