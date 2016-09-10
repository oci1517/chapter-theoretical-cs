import unittest
from quicksort1 import *

class TestQuicksort(unittest.TestCase):

    def test_random(self):
        original = [1,4,2,6,7,8,3]
        correct = original[:]
        quicksort(original)
        self.assertListEqual(original, sorted(correct))

    def test_sorted(self):
        original = [1,2, 2, 3, 4, 5, 6]
        correct = original[:]
        quicksort(original)
        self.assertListEqual(original, sorted(correct))

    def test_reversed(self):
        original = [6,5,4,3,2,1,1]
        correct = original[:]
        quicksort(original)
        self.assertListEqual(original, sorted(correct))

    def test_dupplicates(self):
        original = [1,2,1,2,2,1,4,1,2,3]
        correct = original[:]
        quicksort(original)
        self.assertListEqual(original, sorted(correct))


if __name__ == '__main__':
    unittest.main()
