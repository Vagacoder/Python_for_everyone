##
#  This program computes Fibonacci numbers using a recursive function.
#
# R11.9 add a global variable to record the times of fib() called

# global variable
count = 0

def main() :
    global count      # need global variable
    
    n = int(input("Enter n: "))
    for i in range(1, n + 1) :
        count = 0
        f = fib(i)
        print("fib(%d) = %d" % (i, f))

## Computes a Fibonacci number.
#  @param n an integer
#  @return the nth Fibonacci number
#
def fib(n) :
    global count
    count += 1
    
    if n <= 2 :
        print("fib() is called", count, "times")
        return 1
    else :
        print("fib() is called", count, "times")
        return fib(n - 1) + fib(n - 2)
      
# Start the program.
main()
