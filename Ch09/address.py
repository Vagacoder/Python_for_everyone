## Ch09 Address class for P9.4

class Address:
    
    def __init__(self, apartment = ''):
        self._houseNumber = ''
        self._streetName = ''
        self._apartment = apartment
        self._city = ''
        self._state = ''
        self._postalCode = ''

    def print(self):
        print(self._houseNumber, self._streetName)
        print(self._city, self._state, self._postalCode)

    def comesBefore(self, other):
        if self._postalCode < other._postalCode:
            return True
        else:
            return False
    