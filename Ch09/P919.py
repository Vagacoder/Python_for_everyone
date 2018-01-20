## Ch09 P9.19

class CashRegister :

    def __init__(self) :
        self._itemPriceList = []
      

    def addItem(self, price) :
        self._itemPriceList.append(price)
      

    def getTotal(self) :
        totalPrice = 0
        for price in self._itemPriceList:
            totalPrice += price
        return totalPrice
      
    def getCount(self) :
        return len(self._itemPriceList)
 
    def clear(self) :
        self._itemPriceList.clear()
     
    def getDollar(self):
        return int(self.getTotal())
    
    
    def displayAll(self):
        for price in self._itemPriceList:
            print('$%.2f' %price)
    