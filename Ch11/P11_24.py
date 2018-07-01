# # P11.24
# backtracking for summation puzzle
import re
from Ch11.P11_14 import PermutationIterator
# import Ch11.P11_14

class SummationPuzzle:

    def __init__(self, formula):
        self._NUMBERS = "0123456789"
        self._formula = formula
        self._letters = ""
        for cha in self._formula:
            if cha not in self._letters and cha.isalpha():
                self._letters += cha

        if len(self._letters) > 10:
            raise ValueError('Input formula has more than 9 unqiue letters!')
        else:
            self._letters += "*" * (10 - len(self._letters))

        print(self._letters)
        self._per_iter = PermutationIterator(self._letters)


    def solv(self):
        print(self._formula)
        done = False

        while not done:
            results = self.extend()
            print(results)
            for r in results:
                done = self.examin(r)
                if done:
                    print(r)


    def extend(self):
        resultList = []
        if self._per_iter.has_more_permutation():
            permLetters = self._per_iter.next_permutation()
            #print(permLetters)
            for permLetter in permLetters:
                result = self._formula
                for i in range(len(permLetter)):
                    result = result.replace(permLetter[i], str(i))
                    #print(result)
                    resultList.append(result)

        return resultList


    def examin(self, formulaReplaced):
        formulaSplit = re.split("\+|=", formulaReplaced)
        augend = formulaSplit[0].strip()
        addend = formulaSplit[1].strip()
        result = formulaSplit[2].strip()
        if augend.isdigit() and addend.isdigit() and result.isdigit():
            return augend + addend == result
        else:
            return False


def main():
    sp1 = SummationPuzzle("send + more = money")
    sp1.solv()


main()