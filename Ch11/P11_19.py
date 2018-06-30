# # P11.19, also include P11.23, the constructor accept n as argument
# class of generic Partial Solution

class PartialSolution:

    def __init__(self, queens = 4):

        self._NQUEENS = queens
        self._COLUMNS = "abcdefghijklmnopqrstuvwxyz"[:queens]
        self._ACCEPT = 1
        self._CONTINUE = 2
        self._ABANDON = 3

    def solve(self, partialSolution):
        exam = self.examine(partialSolution)
        if exam == self._ACCEPT:
            print(partialSolution)

        elif exam != self._ABANDON:
            for p in self.extend(partialSolution):
                self.solve(p)


    def examine(self, partialSolution):
        for i in range(0, len(partialSolution)):
            for j in range(i + 1, len(partialSolution)):
                if self.attacks(partialSolution[i], partialSolution[j]):
                    return self._ABANDON
        if len(partialSolution) == self._NQUEENS:
            return self._ACCEPT
        else:
            return self._CONTINUE


    def extend(self, partialSolution):
        results = []
        row = len(partialSolution) + 1
        for column in self._COLUMNS:
            newSolution = list(partialSolution)
            newSolution.append(column + str(row))
            results.append(newSolution)
        return results


    def attacks(self, p1, p2):
        column1 = self._COLUMNS.index(p1[0]) + 1
        row1 = int(p1[1])
        column2 = self._COLUMNS.index(p2[0]) + 1
        row2 = int(p2[1])
        return (row1 == row2 or column1 == column2 or
                abs(row1 - row2) == abs(column1 - column2))


class EightQueensPartialSolution(PartialSolution):

    def __init__(self):
        super().__init__(8)


def main():
    p4 = PartialSolution()
    p4.solve([])
    p8 = EightQueensPartialSolution()
    p8.solve([])

main()
