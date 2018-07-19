## P12.9

# Bentley and McIlroy improvement on quick sort

def quickSort(values, start, to):
    if start >= to:
        return

    p = partition(values, start, to)
    quickSort(values, start, p)
    quickSort(values, p + 1, to)


# suggestion on partition from "<= | >=" to "< | = | >"

def partition(values, start, to):
    pivot = values[start]
    i = start - 1
    j = to + 1
    while i < j:
        i = i + 1
        while values[i] < pivot:
            i = i + 1
        j = j - 1
        while values[j] > pivot:
            j = j - 1

        if i < j:
            # Swap the two elements
            temp = values[i]
            values[i] = values[j]
            values[j] = temp
    return j