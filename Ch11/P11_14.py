# # P11.14
# Permutation using loop

class PermutationIterator:

    def __init__(self, input):
        self._string = input

    def next_permutation(self):
        # todo


    def has_more_permutation(self):
        if len(self._string) > 0:
            return True
        else:
            return False


def main():
    per_iter = PermutationIterator("eat")
    while per_iter.has_more_permutation():
        print(per_iter.next_permutation())


main()