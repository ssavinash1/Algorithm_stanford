import unittest

from src.quick_sort import quick_sort, partition, pick_pivot


class QuickSortTest(unittest.TestCase):

    def test_partition_splits_array_by_pivot(self):
        arr = [3, 8, 2, 5, 1, 4, 7, 6]
        expected = [1, 2, 3, 5, 8, 4, 7, 6]
        actual, pos = partition(arr, 0, len(arr))
        self.assertEqual(actual, expected, 'partition subroutine works')
        self.assertEqual(pos, 2, 'return the final position of the pivot elem')

    def test_pick_pivot(self):
        pivot = pick_pivot(1, 10)
        self.assertIn(pivot, range(1, 11), 'pivot is picked randomly')

    def test_quick_sort(self):
        arr = [4, 6, 5, 3 ,7, 8, 1, 9, 2, 0]
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        actual = quick_sort(arr, 0, len(arr)-1)
        self.assertEqual(actual, expected, 'quick sort sorts the array')
