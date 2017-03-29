import unittest
from path_finder import *

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
        finder = PathFinder(5, 5, [(2,1)], [])
        self.assertEqual(finder.number_of_paths(), 40)

    def test_jumps(self):
        """
            TEST CASE:
            5 5 () (((2,1),(0,3)))
        """
        finder = PathFinder(5, 5, [], [((2,1),(0,3))])
        self.assertEqual(finder.number_of_paths(), 55)

    def test_1by5(self):
        """
            TEST CASE:
            1 5 () (((0,1),(0,4)))
        """
        finder = PathFinder(1, 5, [], [((0,1),(0,4))])
        self.assertEqual(finder.number_of_paths(), 1)
        self.assertEqual(finder.get_paths(), '[(0, 0), (0, 1), (0, 4)]')


    def test_no_solution(self):
        """
            TEST CASE:
            2 2 ((0,1),(1,0)) ()
        """
        finder = PathFinder(2, 2, [(1,0),(0,1)], [])
        self.assertEqual(finder.number_of_paths(), 0)

    def test_correct_path(self):
        """
            TEST CASE:
            3 3 ((0,1),(1,1)) ()
        """
        finder = PathFinder(3, 3, [(0,1),(1,1)], [])
        self.assertEqual(finder.number_of_paths(), 1)
        self.assertEqual(finder.get_paths(), '[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]')


if __name__ == '__main__':
    unittest.main()
