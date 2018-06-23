# this tests instance variable in a class
import Function1

class Sample:

    _className = "class name"

    def __init__(self):
        self._number = 0
        self._name = "instance name"
        total = 0

    def calculation(self):
        # self._number += 1
        # print(self._number)
        total = "here"
        print(total)
        print(Sample._className)

    def calculation1(self):
        _name = "local name"
        print(self._number)
        print(self._name)
        print(_name)


def main():
    s1 = Sample()
    s2 = s1.__init__()
    s1.calculation()
    s1.calculation1()
    print(Function1.isInteger(10))
    print(str(Function1.isInteger(10)))

main()