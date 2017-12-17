#This program computes the volume (in liters) of a six-pack of soda
# cans and the total volume of a six-pack and a two liter bottle.

#Liter in a 12 ounce can and a two-liter bottle.
CAN_VOLUME =0.355
BOTTLE_VOLUME = 2.0

#Number of cans per pack
cansPerPack = 6

totalVolume = cansPerPack * CAN_VOLUME
print('A six-pack of 12-ounce cans contains', totalVolume, 'liters.')

totalVolume = totalVolume + BOTTLE_VOLUME
print('A six-pack and a two-liter bottle contain', totalVolume,'liters.')

unitPrice = 1.99
quantity = 12
totalPrice = unitPrice*quantity
print('The total payment for your purchase is', totalPrice,'.')
