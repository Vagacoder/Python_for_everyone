## country class for P12.13

class Country:

    def __init__(self, name, area):
        self._name = name
        self._area = area


    def __lt__(self, other):
        return self._area < other.getArea()


    def getArea(self):
        return self._area

    def getName(self):
        return self._name