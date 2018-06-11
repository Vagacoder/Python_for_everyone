## Ch09 Address class for P9.4

class Address:

    _addressNumber = 0
    
    def __init__(self, apartment = '', streetName = ''):
        self._houseNumber = ''
        self._streetName = streetName
        self._apartment = apartment
        self._city = ''
        self._state = ''
        self._postalCode = ''
        Address._addressNumber += 1

    def print(self):
        print(self._houseNumber, self._streetName)
        print(self._city, self._state, self._postalCode)

    def comesBefore(self, other):
        if self._postalCode < other._postalCode:
            return True
        else:
            return False

    def howManyAddress(self):
        return Address._addressNumber

    # Override
    def __repr__(self):
        return self._houseNumber +" " + self._streetName + " "+self._city + " " + self._state + " " + self._postalCode

add1 = Address("Apt. 4", "Hollister Ave")
add2 = Address("Apt. 2", "De la vina Street")
add1.print()
add2.print()
print(add1.howManyAddress())
print(add2.howManyAddress())
print(add1)