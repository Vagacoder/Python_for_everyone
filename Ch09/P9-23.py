## Ch09 P9.23

from country import Country

inFilePop = open('worldpop.txt', 'r')
inFileArea = open('worldarea.txt', 'r')
countries = []

line = inFilePop.readline()
line1 = inFileArea.readline()
while line != '':
    data = line.rsplit(' ', 1)
    data1 = line1.rsplit(' ',1)
    newCountry = Country(name = data[0].strip(), pop = int(data[1].strip()), area = int(data1[1].strip()))
    countries.append(newCountry)
    line = inFilePop.readline()
    line1 = inFileArea.readline()


largestArea = (countries[0].getName(), countries[0].getArea())
largestPop = (countries[0].getName(), countries[0].getPop())
largestDensi = (countries[0].getName(), countries[0].getDensity())

for i in countries:
    name = i.getName()
    if i.getArea() > largestArea[1]:
        largestArea = (name, i.getArea())
    
    if i.getPop() > largestPop[1]:
        largestPop = (name, i.getPop())

    if i.getDensity() > largestDensi[1]:
        largestDensi = (name, i.getDensity())

print(largestArea)
print(largestPop)
print(largestDensi)

inFilePop.close()
inFileArea.close()
