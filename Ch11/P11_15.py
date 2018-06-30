## P11.15
# permutation for a list of integers


def main():
    # integer permutation
    NUM_ELEMENTS = 4
    a = list(range(1, NUM_ELEMENTS + 1))
    print(a)
    while nextPermutation(a):
        print(a)

    # string permutation
    string1 = "eat"
    b = list(range(1, len(string1)+1))

    for i in b:
        print(string1[i-1])

    print(b)
    for i in b:
        print(string1[i-1], end="")
    print()

    while nextPermutation(b):
        for i in b:
            print(string1[i - 1], end="")
            if i == b[-1]:
                print()


def nextPermutation(a):
    i = len(a) - 1
    while i > 0:
        if a[i - 1] < a[i]:
            j = len(a) - 1
            while a[i - 1] > a[j]:
                j = j - 1
            swap(a, i - 1, j)
            reverse(a, i, len(a) - 1)
            return True
        i = i - 1
    return False


def reverse(a, i, j):
    while i < j:
        swap(a, i, j)
        i = i + 1
        j = j - 1


def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


main()