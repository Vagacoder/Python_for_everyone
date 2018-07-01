# # P11.14
# Permutation using loop


class PermutationIterator:

    def __init__(self, input1):
        self._string = input1
        self._index = 0

    def next_permutation(self):
        shorter = self._string[:self._index] + self._string[self._index +1:]
        tailIterator = PermutationIterator(shorter)
        shortPermu = set()
        shortPermu.add("")
        result = set()
        while tailIterator.has_more_permutation():
            shortPermu = tailIterator.next_permutation()

        for i in shortPermu:
            result.add(self._string[self._index] + i)
            result.add(i + self._string[self._index] )

        self._index += 1
        return result

    def has_more_permutation(self):
        if self._index < len(self._string):
            return True
        else:
            return False


def main():
    per_iter = PermutationIterator("feat")
    while per_iter.has_more_permutation():
        print(per_iter.next_permutation())


main()