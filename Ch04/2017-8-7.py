##Ch04 P4.2

total = 0
count_even = 0
count_odd = 0


num_raw = input('Plese enter an integer (Q for finish): ')

if num_raw == 'Q' or num_raw == 'q' or num_raw == '':
    exit('Thanks for using this program.')
try:
    test1 = int(num_raw)
except:
    exit('Wrong input, please try again.')

if num_raw != '' and num_raw != 'Q' and num_raw !='q':
    small = int(num_raw)
    large = int(num_raw)
    num = int(num_raw)-1
    previous1 = num
    previous2 = int(num_raw)-2

while num_raw != '' and num_raw != 'Q' and num_raw !='q':
    num = int(num_raw)

    if num < small:
        small = num
    if num > large:
        large = num

    if num%2 == 0:
        count_even += 1
    elif num%2 == 1:
        count_odd += 1

    total += num
    print('Current total is: %d' %total)

    if previous1 == num and previous2 != previous1:
        pre_print = previous1
        print('duplicate is: %d' %pre_print)

    num_raw = input('Plese enter an integer (Q for finish): ')
    previous2 = previous1
    previous1 = num

print('Smallest is:', small)
print('Largest is:', large)
print('There are %d even numbers.' %count_even)
print('There are %d odd numbers.' %count_odd)