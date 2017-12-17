## Ch06 SC30

def main():
    values = [9, 13, 21, 4, 64, 11, 7, 1, 3]

    i= 0
    j= len(values) -1
    while i<j:
        swap(values, i, j)
        i += 1
        j -= 1

    print(values)

def swap(a, i, j) :
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

main()