## Ch02 P2.10

MILEAGE_PER_YEAR = 12000
GAS_PRICE = 2.79

class Car:

    price = 0
    milePerGallon = 0
    resalePrice = 0
    def cost(self, carname):
        yourCost = self.price - self.resalePrice + GAS_PRICE*MILEAGE_PER_YEAR/self.milePerGallon
        print('Your 4-year cost on %-20s %10.2f'%(carname+' is:',yourCost))


car1 = Car()
car1.price = 37500
car1.milePerGallon = 40
car1.resalePrice = 22688
car1.cost('Avalon Hybrid')

car2 = Car()
car2.price = 33500
car2.milePerGallon = 21
car2.resalePricece = 20532
car2.cost('Avalon')


