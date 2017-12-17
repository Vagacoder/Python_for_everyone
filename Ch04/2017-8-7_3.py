## Ch04 SC25

RATE = 5.0
INITIAL_BALANCE = 10000.0


numYears = int(input("Enter number of years: "))

balance = INITIAL_BALANCE

year = 1

while year <= numYears:
    interest = balance * RATE / 100
    balance = balance + interest
    print("%4d %10.2f" % (year, balance))
    year += 1