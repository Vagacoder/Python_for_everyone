## Ch09 P9.1 and P9.2

from counter import Counter

c1 = Counter()
c1.click()
c1.setLimit(10)
c1.click()
c1.click()
print(c1.getValue())
c1.undo()
print(c1.getValue())
c1.undo()
print(c1.getValue())
c1.undo()
print(c1.getValue())
c1.undo()
print(c1.getValue())
c1.click()
c1.click()
c1.click()
c1.click()
c1.click()
print(c1._value)
c1.click()
c1.click()
c1.click()
c1.click()
c1.click()
c1.click()
c1.click()
print(c1._value)
print(str(c1))