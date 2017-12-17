## R4.15

first_name = input('Please enter first name (END for finish): ')
last_name = input('Please enter last name (END for finish): ')

while first_name != 'END' and last_name != 'END':

    score = int(input('Please enter score (-1 for finish): '))
    total = 0
    count = 0

    while score != -1:
        total += score
        count += 1

        score = int(input('Please enter score (-1 for finish): '))

    print ('%s %s total score is %d and average is %.2f.' %(first_name, last_name, total, total/count))

    first_name = input('Please enter first name (END for finish): ')
    last_name = input('Please enter last name (END for finish): ')

## R4.16
s = 0
for i in range(1,10):
    s = s + i
print(s)

count = 1
while s < 10:
    s += count
    count += 1
print(s)


