# Author : Mrunal Nirajkumar Shah
# Traditional or Classical Brute Force Search Algorithm

class ClassicalSearch:
    @staticmethod
    def classical_brute_force_search(array, target):
        """
        Classical brute force search algorithm.
        Returns the index of the target if found, otherwise returns -1.
        """

        for i, item in enumerate(array):
            if item == target:
                return i

        return -1
    