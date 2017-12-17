## Ch02 R2.19

WEEK = 'SunMonTueWedThuFriSat'

#inputNum = int(input('Please enter the number(0-6): '))
inputNum = 2
dayNum1 = inputNum*3
print('%s%s%s' %(WEEK[dayNum1],WEEK[dayNum1+1],WEEK[dayNum1+2]))
print(WEEK[dayNum1]+WEEK[dayNum1+1]+WEEK[dayNum1+2])


## Ch02 R2.20

myString = 'We are good students! We are learning Python hard!'
l1 = 'e'
l2 = 'a'
print(myString)

myString1 = myString.replace(l1,'*')
print(myString1)
print(myString.replace(l2,'*'))

print(myString.replace(l2,l1))
myString2 = myString1.replace(l2,l1)
print(myString2)
print(myString2.replace('*',l2))

