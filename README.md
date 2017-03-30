# 2D-Graph-Traversal

Finds all paths through 2D n by m grid based on a list of blocked points and a list of detours (from point a to point b).
* built in python 3.x

# PathFinder

##### Arguments
The PathFinder class takes in arguments:
* `n` and `m` the dimensions of the sub-space
* `blocks` a list of blocked points (ex: `[(2, 1), (1,2)]` cannot travel through points 2,1 or 1,2
* `detours` a list of detours (ex: `[((2,1), (0, 3))]` will jump from point 2,1 to point 0,3 if landed on)

##### Methods
* `number_of_paths()` returns the number of possible paths through the grid
* `get_paths()` returns a list of all possible paths through the grid

##### Example Usage

     # initializes a 1x5 grid, a block at point 0,3, and a single jump
     > finder = PathFinder(1, 5, [(0,3)], [((0,1),(0,4))])
     > print(finder.number_of_paths())
     1
     > print(finder.get_paths())
     [[(0, 0), (0, 1), (0, 4)]]
     
     > finder = PathFinder(2, 2, [], [])
     > finder.number_of_paths()
     2

# Unit Tests

A unit test suite is provided to test the functionality of the PathFinder class and can be run from the command line...

    > python unit_test.py
    
    ......
    ----------------------------------------------------------------------
    Ran 6 tests in 0.003s

    OK

Tests can be added to `unit_test.py` with the simple structure below

    def test_blocks(self):
        """
            TEST CASE:
            5 5 ((2,1)) ()
        """
        finder = PathFinder(5, 5, [(2,1)], [])
        self.assertEqual(finder.number_of_paths(), 40)


