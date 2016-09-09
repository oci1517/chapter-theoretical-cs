import unittest
from merge_sort_2 import merge_sort

class TestMergeSort(unittest.TestCase):

    def test_random(self):
        self.assertListEqual(
            merge_sort([4,5,2,3,1,6]),
            [1,2,3,4,5,6]
        )

    def test_multiple(self):
        self.assertListEqual(
            merge_sort([1,2,1,2,3,2,1]),
            [1,1,1,2,2,2,3]
        )

    def test_reversed(self):
        self.assertListEqual(
            merge_sort([6,5,4,3,2,1]),
            [1,2,3,4,5,6]
        )


if __name__ == '__main__':
    unittest.main()
