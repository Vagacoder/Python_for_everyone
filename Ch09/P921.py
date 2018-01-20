## Ch09 P9.21


class CashRegister :

    def __init__(self) :
        self._itemPriceList = []
        self._sales = []
      

    def addItem(self, price) :
        self._itemPriceList.append(price*100)
      

    def getTotal(self) :
        totalPrice = 0
        for price in self._itemPriceList:
            totalPrice += price
        
        self._sales.append(totalPrice)
        return totalPrice/100.0


    def getCount(self) :
        return len(self._itemPriceList)


    def clear(self) :
        self._itemPriceList.clear()


    def getDollar(self):
        return int(self.getTotal())
    
    
    def displayAll(self):
        for price in self._itemPriceList:
            print('$%.2f' %(price/100.0))
    
    def getSalesTotal(self):
        totalSale = 0
        for sale in self._sales:
            totalSale += sale
        
        return totalSale/100.0
    
    def getSalesCount(self):
        salesCount = len(self._sales)
        return salesCount
    
    
    def resetSales(self):
        self._sales.clear()

        