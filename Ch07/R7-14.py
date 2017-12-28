##Ch07 R7.14

name = 'Toaster'
qty = 3
price = 29.95

print('%-20s%-5s%-10s%-10s' %('Item', 'Qty', 'Price', 'Total'))
print('%-20s%-5d$%-9.2f$%-9.2f' %(name, qty, price, qty*price))

