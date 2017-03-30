import unittest
from path_finder import *
from count_paths import *


class TestPathFinder(unittest.TestCase):

    def test_2by2(self):
        """
            TEST CASE:
            2 2 () ()
        """
        finder = PathFinder(2, 2, [], [])
        self.assertEqual(finder.number_of_paths(), 2)

    def test_blocks(self):
        """
            TEST CASE:
            5 5 ((2,1)) ()
        """
        finder = PathFinder(5, 5, [(2, 1)], [])
        self.assertEqual(finder.number_of_paths(), 40)

    def test_jumps(self):
        """
            TEST CASE:
            5 5 () (((2,1),(0,3)))
        """
        finder = PathFinder(5, 5, [], [((2, 1), (0, 3))])
        self.assertEqual(finder.number_of_paths(), 55)

    def test_1by5(self):
        """
            TEST CASE:
            1 5 () (((0,1),(0,4)))
        """
        finder = PathFinder(1, 5, [], [((0, 1), (0, 4))])
        self.assertEqual(finder.number_of_paths(), 1)
        self.assertEqual(finder.get_paths(), '[(0, 0), (0, 1), (0, 4)]')

    def test_no_solution(self):
        """
            TEST CASE:
            2 2 ((0,1),(1,0)) ()
        """
        finder = PathFinder(2, 2, [(1, 0), (0, 1)], [])
        self.assertEqual(finder.number_of_paths(), 0)

    def test_correct_path(self):
        """
            TEST CASE:
            3 3 ((0,1),(1,1)) ()
        """
        finder = PathFinder(3, 3, [(0, 1), (1, 1)], [])
        self.assertEqual(finder.number_of_paths(), 1)
        self.assertEqual(finder.get_paths(), '[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]')

    def test_quick_count(self):
        """
            TEST CASE:
            quick count large grid
        """
        finder = PathFinder(50, 50, [], [])
        self.assertEqual(finder.number_of_paths(), 25477612258980856902730428600)

    def test_quick_count_with_blocks(self):
        """
            TEST CASE:
        """
        finder = PathFinder(50, 50, [(25, 25)], [])
        self.assertEqual(finder.number_of_paths(), 21401173121235900936646037400)

if __name__ == '__main__':
    unittest.main()
