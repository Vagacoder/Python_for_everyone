## Ch02 How to 2.1

bill = float(input('Please insert the bill, 1=$1 bill, 5=$5 bill: '))
price = float(input('Please enter the price of item: '))

totalChange = bill - price
dollarChange = totalChange//1
quarterChange = totalChange%1//0.25

print('Dollars for change:  %5d'%(dollarChange))
print('Quarters for change: %5d'%(quarterChange))
