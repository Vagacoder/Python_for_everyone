## Ch08 P8.7

from polynomial import newPolynomial, addTerm, multiply
    
p = newPolynomial(-10, 0)
addTerm(p, -1, 1)
addTerm(p, 9, 7)
addTerm(p, 5, 10)

print(p)

q = multiply(p, p)

print(q)
