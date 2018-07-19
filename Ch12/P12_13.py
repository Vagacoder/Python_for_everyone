## P12.13

from Ch12.country import Country


def main():
    c1 = Country("USA", 10000)
    c2 = Country("France", 5000)
    c3 = Country("Russian", 20000)
    c4 = Country("Germany", 4500)
    c5 = Country("Aus", 8000)

    clist = [c1, c2, c3, c4, c5]

    for c in clist:
        print(c.getName())

    clist1 = sorted(clist)
    print()

    for c in clist1:
        print(c.getName())


main()