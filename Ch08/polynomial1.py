## Ch08 P8.8
# module for P8-8.py using dictionary


def newPolynomial(coefficient, power):
    
    polynomial = {}
    polynomial[power] = coefficient
    
    return polynomial


def addTerm(polyDict, coefficient, power):

    for oldPower in polyDict:
        
        if oldPower == power:
            polyDict[oldPower] += coefficient
            return polyDict
    
    polyDict[power] = coefficient
    
    return polyDict


def multiply(polyDict1, polyDict2):
    
    newDict = {}
    
    for power1 in polyDict1:
        for power2 in polyDict2:
            newPower = power1 + power2
            newCoefficient = polyDict1[power1] * polyDict2[power2]
            addTerm(newDict, newCoefficient, newPower)
    
    return newDict


