##Ch06 P6.32

def nameOfBestCustomer(sales, customers):

    maxSale = max(sales)
    index = sales.index(maxSale)
    return (customers[index], maxSale)
        
    

nameList = []
priceList = []

price = int(input('Please enter the price (0 for finish): '))

while price>0:
    priceList.append(price)
    name = input('Please enter the name of customer: ')
    nameList.append(name)
    price = int(input('Please enter the price (0 for finish): '))

(bestC, maxSale) = nameOfBestCustomer(priceList, nameList)
print('The best customer today is %s, with purchase of $%.2f.' %(bestC, maxSale))
