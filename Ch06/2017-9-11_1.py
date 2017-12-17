## Ch06 R6.24

def main() :
    values = [9, 13, 21, 4, 11, 7, 1, 3]
    i = 0
    j = len(values) // 2
    while i < len(values) // 2 :
        #swap(values, i, j)
        #i = i + 1
        #j = j + 1
        values.append(values.pop(0))
        i +=1


    print(values)

def swap(a, i, j) :
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

main()