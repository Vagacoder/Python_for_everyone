## Ch02 P2.12

#drive = input('Please enter the drive: ')
#path = input('Please enter the path: ')
#fileName = input('Please enter the file name: ')
#fileExtension = input('Please enter the file extension: ')

#print('%s:%s\\%s.%s' %(drive.upper(), path, fileName, fileExtension))

## Ch02 P2.13 2.14

number = input('Please enter an integer between 10,000 and 99,999: ')
print(number.replace(',',''))
print(number[0]+number[1]+number[3]+number[4]+number[5])


num = input('Please enter an integer between 1000 and 999999: ')
length = len(num)
num1 = int(num)
numAbove1000 = num1//1000
numBelow1000 = num1%1000
print('%d,%03d'%(numAbove1000,numBelow1000))
print('%d%03d'%(numAbove1000,numBelow1000))
num2 = int('%d%03d'%(numAbove1000,numBelow1000))
print(num2*3)

