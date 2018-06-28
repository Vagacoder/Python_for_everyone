# -*- coding: utf-8 -*-

## sc12 and sc13
## recursive sum

# sc12
def sumList(numbers, index):
    if index >= len(numbers):
        return 0
    elif index == len(numbers)-1:
        return numbers[len(numbers)-1]
    else:
        return numbers[index] + sumList(numbers, index + 1)
                       
# sc13
def sumList1(numbers):
    if len(numbers) <= 0:
        return 0        
    elif len(numbers) == 1:
        return numbers[0]
    else:
        newNumbers = list(numbers)
        newNumbers.pop(0)
        return numbers[0] + sumList1(newNumbers)
        
        
def main():
    alist = [1,2,3,4,5,6,7,8,9,10]
    print(sumList(alist, 0))
    print(sumList1(alist))


main()