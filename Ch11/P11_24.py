# # P11.24
# this is not a backtracking for summation puzzle
# this is breadth first method, which is low efficiency
# since the first step of generating all permutation taking too much memory
# will try a real backtracking method
import re


class SummationPuzzle:

    # constructor
    def __init__(self, formula):

        self._formula = formula

        # generate a string with all unique letters from formula
        self._letters = ""
        for cha in self._formula:
            if cha not in self._letters and cha.isalpha():
                self._letters += cha

        # fill unique letters string with "*" up to length == 10
        if len(self._letters) > 10:
            raise ValueError('Input formula has more than 9 unqiue letters!')
        else:
            self._letters += "*" * (10 - len(self._letters))

        # print(self._letters)

    # solv method
    def solv(self):
        print(self._formula)
        results = self.extend()

        for r in results:
            if self.examin(r):
                print(r)

    # call permutation method to generate all possible digitalized formula
    def extend(self):
        resultList = []

        # generat all possible permutation of self._letters
        permLetters = permutations(self._letters)

        for permLetter in permLetters:
            result = self._formula
            for i in range(len(permLetter)):
                result = result.replace(permLetter[i], str(i))

            resultList.append(result)

        return resultList

    # check whether the digitalized formula is correct
    def examin(self, formulaReplaced):
        formulaSplit = re.split("\+|=", formulaReplaced)
        augend = formulaSplit[0].strip()
        addend = formulaSplit[1].strip()
        result = formulaSplit[2].strip()
        if augend.isdigit() and addend.isdigit() and result.isdigit():
            return int(augend) + int(addend) == int(result)
        else:
            return False


# imported recursive method to get all permutations for one string
def permutations(word):
    result = []

    # The empty string has a single permutation: itself.
    if len(word) == 0:
        result.append(word)
        return result
    else:
        # Loop through all character positions.
        for i in range(len(word)):
            # Form a shorter word by removing the ith character.
            shorter = word[: i] + word[(i + 1) :]

            # Generate all permutations of the simpler word.
            shorterPermutations = permutations(shorter)

            # Add the removed character to the front of each permutation
            # of the simpler word.
            for string in shorterPermutations:
                result.append(word[i] + string)

        # Return all permutations.
        return result


# main method to execute
def main():
    sp1 = SummationPuzzle("send + more = money")
    # sp1 = SummationPuzzle("base + ball = games")
    # sp1 = SummationPuzzle("kyoto + osaka = tokyo")
    sp1.solv()


main()
