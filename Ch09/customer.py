## Class Customer for Ch09 P9.26 and P9.27

class Customer:
    
    def __init__(self):
        self._totalPurchase = 0.0
        self._PURCHASE_CAP = 100.0
        self._DISCOUNT = 10.0
        self._shopSet = set()
        
        
    def makePurchase(self, amount, shop):
        if self.discountReached():
            amount = amount - self._DISCOUNT
            self._totalPurchase = 0
            self._shopSet.clear()
        else:            
            self._totalPurchase += amount
            self._shopSet.add(shop)
        
        return amount
        
    def discountReached(self):
        if self._totalPurchase >= self._PURCHASE_CAP and len(self._shopSet)>=3:          
            return True  
        else:
            return False
        
        
        

