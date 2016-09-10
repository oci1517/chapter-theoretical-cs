import unittest
from quicksort import *

class TestQuicksort(unittest.TestCase):

    def test_random(self):
        original = [1,4,2,6,7,8,3]
        correct = original[:]
        quicksort(original)
        self.assertListEqual(quicksort(original), sorted(correct))

    def test_sorted(self):
        original = [1,2, 2, 3, 4, 5, 6]
        correct = original[:]
        quicksort(original)
        self.assertListEqual(quicksort(original), sorted(correct))

    def test_sorted(self):
        original = [6,5,4,3,2,1,1]
        correct = original[:]
        quicksort(original)
        self.assertListEqual(quicksort(original), sorted(correct))

    def test_sorted(self):
        original = [1,2,1,2,2,1,4,1,2,3]
        correct = original[:]
        quicksort(original)
        self.assertListEqual(quicksort(original), sorted(correct))

# 
# class TestPartition(unittest.TestCase):
#
#     def test_random(self):
#         original = [1,4,2,6,7,8,3]
#         left = 0
#         right = len(original) - 1
#         correct = [1,2,3,6,7,8,4]
#
#         partition(original, left, right, right)
#
#         self.assertListEqual(original, correct)
#
#     def test_dupplicate(self):
#         original = [5,4,6,2,4,8,6,2]
#         left = 0
#         right = len(original) - 1
#         correct = [2, 2, 6, 5, 4, 8, 6, 4]
#
#         partition(original, left, right, right)
#
#         self.assertListEqual(original, correct)


if __name__ == '__main__':
    unittest.main()
