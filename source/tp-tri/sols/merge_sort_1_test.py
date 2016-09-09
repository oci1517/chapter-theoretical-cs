import unittest
from merge_sort_1 import merge_sort, merge, insert

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


class TestInsert(unittest.TestCase):

    test_list = [4,5,7]

    def test_insert_small(self):
        self.assertListEqual(insert(3, self.test_list), [3,4,5,7])

    def test_insert_middle(self):
        self.assertListEqual(insert(6, self.test_list), [4,5,6,7])

    def test_insert_large(self):
        self.assertListEqual(insert(8, self.test_list), [4,5,7,8])

class TestMerge(unittest.TestCase):

    def test_merge_small(self):
        self.assertListEqual(merge([1], [2]), [1,2])

    def test_merge_small_reversed(self):
        self.assertListEqual(merge([2], [1]), [1,2])

    def test_merge_more(self):
        self.assertListEqual(merge([1, 3], [2]), [1,2,3])
        self.assertListEqual(merge([1, 3], [2, 3]), [1,2,3,3])
        self.assertListEqual(merge([1, 3, 5], [2, 3, 4]), [1,2,3,3,4,5])


if __name__ == '__main__':
    unittest.main()
