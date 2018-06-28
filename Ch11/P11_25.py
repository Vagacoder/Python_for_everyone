## P11.25
#
fibList = dict()

def main() :
    global fibList
    n = int(input("Enter n: "))
    fibList.clear()
    for i in range(1, n + 1) :
        f = fib(i)
        print("fib(%d) = %d" % (i, f))

## Computes a Fibonacci number.
#  @param n an integer
#  @return the nth Fibonacci number
#
def fib(n) :
    global fibList
    if n <= 2 :
        fibList[n] = 1
        return 1
    else :
        if n-1 in fibList and n-2 in fibList:
            return fibList.get(n-1) + fibList.get(n-2)
        else:
            n_1 = fib(n-1)
            n_2 = fib(n-2)
            fibList[n] = n_1 + n_2
            return n_1 + n_2
      
# Start the program.
main()
