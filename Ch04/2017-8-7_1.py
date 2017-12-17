## Cho4 SC 22

total = 0
count = 0

num = input('Please enter a integer (press ENTER to finish): ')

while num != '':
    num1 = int(num)
    if num1 > 0:
        total += num1
        count += 1

    num = input('Please enter a integer: ')

print('Total positive number is: %d' %total)

