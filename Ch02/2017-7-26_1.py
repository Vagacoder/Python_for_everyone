## Ch02 P2.11

tankCapacity = float(input('Please enter the tank capacity of your car(in gallon): '))
milePerGallon = float(input('Please enter how many miles per gallon your car can drive: '))
gasPrice = float(input('Please enter the current gas price(dollar per gallon): '))
carModel = input('Please enter the model of your car: ')

class Car:

    def cost100mile(self):
        cost = 100 / milePerGallon * gasPrice
        print('It costs %.2f dollars for %s to drive 100 miles.'%(cost, carModel))

    def mileage(self):
        mile1Tank = tankCapacity * milePerGallon
        print('%s can drive %.2f miles with a full tank.' %(carModel, mile1Tank))

car1 = Car()
car1.cost100mile()
car1.mileage()

