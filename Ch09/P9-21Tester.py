## Ch09 P9.21 tester

from P921 import CashRegister

c1 = CashRegister()
c1.addItem(1.50)
c1.addItem(2.25)
print(c1.getTotal())
print(c1.getCount())
print(c1.getDollar())
c1.displayAll()
print('clearing.... done!')
c1.clear()
c1.displayAll()
print(c1.getSalesTotal())
print(c1.getSalesCount())
