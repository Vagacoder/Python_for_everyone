values = [32, 54, 67.5, 29]
print(values)
values.append(12)
print(values)
print(values[-1])
print(values[-5])
print(values.index(32))
newValue = [34,87]
print(values + newValue)
new1 = list(newValue)
new1.append(100)
print(new1)
print(newValue)
string1 = "We are here"
print(string1[:])
print(new1)
new1.pop()
print(new1)
list1 = list(list())
print(list1)
list1 = []
list2 = []
list3 = []
table = []
table.append(list1)
table.append(list2)
table.append(list3)
print(table)
print(table, end="&\n\\")
