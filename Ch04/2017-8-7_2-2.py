## Ch04 P4.5
num_raw = input('Please enter a number (enter Q to finish): ')

if num_raw == 'Q' or num_raw == 'q' or num_raw == '' or num_raw.isalpha():
    exit('Thanks for using.')

else:
    num = float(num_raw)
    small = num
    large = num
    total = num
    count = 1
    difference = 0

while num_raw != 'Q' and num_raw != 'q' and num_raw != '' and not num_raw.isalpha():
    num_raw = input('Please enter a number (enter Q to finish): ')
# ths is not a good way, since I need check whether input is Q, and if it is, I need skip



    num = float(num_raw)
    total += num
    count += 1

    if num < small:
        small = num
    if num > large:
        large = num



average = total/count
difference = large - small
print('Average is %.4f.' %average)
print('Smallest is %.4f.' %small)
print('Largest is %.4f.' %large)
print('Difference between smallest and largest is %.2f.' %difference)



