# -*- coding: utf-8 -*-

## P11.11
# recursive squareroot


def squareRoot(x):
    if x > 0:
        return squareRootGuess(x, x/2)
    else:
        return "wrong input"

# recursive help function    
def squareRootGuess(x, g):
    if abs(x - g**2) < 1E-14: # abs() is important!!!
        return g
    else:
        return squareRootGuess(x, (g + x/g)/2)

        
def main():
    print(squareRoot(-1))
    print(squareRoot(0))
    print(squareRoot(16))

main()
      
