## P12.15
# improve binary search function, return -k-1, k is the position before
# which the element should inserted

from random import randint


def binarySearch1(values, low, high, target):
    if low <= high:
        mid = (low + high) // 2
        if values[mid] == target:
            return mid
        elif values[mid] < target:
            return binarySearch1(values, mid + 1, high, target)
        else:
            return binarySearch1(values, low, mid - 1, target)
    else:
        return -low-1


def main():
    n = 20
    values = [1]
    for i in range(1, n):
        values.append(values[i - 1] + randint(1, 100))
    print(values)

    done = False
    while not done:
        target = int(input("Enter number to search for, -1 to quit: "))
        if target == -1:
            done = True
        else:
            pos = binarySearch1(values, 0, len(values) - 1, target)
            if pos < 0:
                print("Not found, position at ", pos)
            else:
                print("Found in position ", pos)


main()
