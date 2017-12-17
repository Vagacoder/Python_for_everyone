## Ch2, test String format operator
#title1 = 'Quantity:'
#title2 = 'Price:'

#print('%10s %10d' %(title1, 24))
#print('%10s %10.2f' %(title2, 17.231))

#print('%-10s %-10d' %(title1, 24))
#print('%-10s %-10.2f' %(title2, 17.231))

## Ch2 SC 22
#age = int(input('Please enter your age: '))

#userInput = input("Please enter the number of cans")
#cans = int(userInput)

## Ch2 sc 26

print('%-10s %5d'%('Bottles:', 8))
print('%-10s %5d'%('Cans:', 24))

## Ch2 R2.10
purchase = 19.93
payment = 20.00
change = payment - purchase
print(round(change, 2))

#print('%.2f'%change)

