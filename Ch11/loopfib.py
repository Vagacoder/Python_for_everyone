##
#  This program computes Fibonacci numbers using an iterative function.
#

def main() :
    n = int(input("Enter n: "))

    for i in range(1, n + 1) :
        count = 0
        f = fib(i, count)
        print("fib(%d) = %d" % (i, f))
        # print("fib() is called", count, "times")

## Computes a Fibonacci number.
#  @param n an integer
#  @return the nth Fibonacci number
#
def fib(n, count) :
    count += 1
    if n <= 2 :
        print("fib() is called", count, "times")
        return 1
    else :
        olderValue = 1
        oldValue = 1
        newValue = 1
        for i in range(3, n + 1) :
            newValue = oldValue + olderValue
            olderValue = oldValue
            oldValue = newValue
        print("fib() is called", count, "times") 
        return newValue
      
# Start the program.
main()
