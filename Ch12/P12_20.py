## sort a list of string by increasing length
# P12.20 and P12.21


def sortStringLength(strings):
    for i in range(1, len(strings)):
        next = strings[i]
        j = i
        while j > 0 and len(strings[j - 1]) >= len(next):
            if len(strings[j - 1]) > len(next):
                strings[j] = strings[j - 1]

            elif len(strings[j - 1]) == len(next):
                if strings[j - 1] > next:
                    strings[j] = strings[j - 1]
                else:
                    break   # this is important: once j-1 is smaller than next, j shouldn't be moved
            j = j - 1

        strings[j] = next


def main():
    a = ["that", "be", "git", "These", "a", "an", "tree", "python", "bee", "increasing", "", "english"]
    sortStringLength(a)
    print(a)


main()
