## Ch09 P9.22

from portfolio import Portfolio

p1 = Portfolio()
p1.deposit(10000, 'c')
p1.deposit(5000, 's')
print(p1.getBalance('c'))
print(p1.getBalance('s'))
