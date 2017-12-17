##Ch06 P6.31

def discount(prices, isPet, nItems):

    petNumber = 0
    itemNumber = 0
    petTotalPrice = 0
    itemTotalPrice = 0
    price = 0
    DISCOUNT_RATE = 0.2

    for i in range(len(isPet)):
        if isPet[i]:
            petNumber += 1
            petTotalPrice += prices[i]

        else:
            itemNumber += 1
            itemTotalPrice += prices[i]

    if petNumber >= 1 and itemNumber >=5:
        price = petTotalPrice + itemTotalPrice * (1-DISCOUNT_RATE)
    else:
        price = petTotalPrice + itemTotalPrice

    return price

prices = []
isPet = []

price = int(input('Please enter the price (-1 for finish): '))
while price >= 0:

    prices.append(price)
    pet = input('Please enter "Y" for pet, "N" for non-pet: ')
    if pet == 'Y':
        isPet.append(True)
    else:
        isPet.append(False)

    price = int(input('Please enter the price (-1 for finish): '))

discountPrice = discount(prices, isPet, 0)
print('The price is %.2f' % discountPrice)
