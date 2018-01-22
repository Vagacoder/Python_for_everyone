##Ch06 P6.33

def nameOfBestCustomer(sales, customers, topN):

    salesRecord = []+sales
    customerRecord = [] + customers
    topNSales = []
    topNCustomer = []

    for i in range(topN):
        if len(salesRecord)>0:
            maxSale = max(salesRecord)
            index = salesRecord.index(maxSale)
            topNSales.append(salesRecord.pop(index))
            topNCustomer.append(customerRecord.pop(index))

    return (topNSales, topNCustomer)
        
    

nameList = []
priceList = []

price = int(input('Please enter the price (0 for finish): '))

while price>0:
    priceList.append(price)
    name = input('Please enter the name of customer: ')
    nameList.append(name)
    price = int(input('Please enter the price (0 for finish): '))

(topNSale, topNCustomer) = nameOfBestCustomer(priceList, nameList, 3)
print(topNSale)
print(topNCustomer)
