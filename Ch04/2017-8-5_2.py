## Ch04 P4.13

num = int(input('Please enter a positive integer: '))
quotient = num
remainder = 0

while quotient > 0:
    remainder = quotient%2
    quotient = quotient//2
    print(remainder)
