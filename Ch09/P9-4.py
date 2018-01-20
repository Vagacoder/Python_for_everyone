## Ch09 P9.4

from address import Address

a1 = Address()
a2 = Address(apartment = '17')

a1._postalCode = '93105'
a2._postalCode = '43101'
print(a2.comesBefore(a1))
