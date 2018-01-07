## Ch08 P8.7
# module for P8-7.py using list


def newPolynomial(coefficient, power):
    
    polynomial = []
    polynomial.append((coefficient, power))
    
    return polynomial


def addTerm(polyList, coefficient, power):

    for i in range(len(polyList)):
        item = polyList[i]
        oldCoefficient = item[0]
        oldPower = item[1]
        if oldPower == power:
            newItem = (coefficient + oldCoefficient, power)
            polyList[i] = newItem
            return polyList
    
    polyList.append((coefficient, power))     
    
    return polyList


def multiply(polyList1, polyList2):
    
    newList = []
    
    for i in polyList1:
        for j in polyList2:
            newTerm = (i[0]*j[0], i[1]+j[1])
            addTerm(newList, newTerm[0], newTerm[1])
    
    return newList
    
