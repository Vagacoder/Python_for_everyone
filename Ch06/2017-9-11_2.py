## Ch06 R6.24

def main() :
    values = [9, 13, 21, 4, 11, 7, 1, 3]
    n = len(values)
    values = values[:n//2] + values[n//2:]

    print(values)


main()