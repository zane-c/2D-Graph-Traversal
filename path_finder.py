import math


class PathFinder:
    """
        The path finder class finds all possible solution
        paths through an n by m grid that might or might
        not have blocked paths or detours. For large grids
        greater than a 100 cells, it quick counts using 
        combinatorics
    """

    def __init__(self, n, m, blocks, detours):
        """
            If grid is too big to find individual paths, quick_count is 
            called and only the number of paths is counted not the specific
            points that comprise that path. If the grid is smaller than 100 
            total cells, find_paths is called.
        """
        if m * n >= 100:
            self.num_paths = self.quick_count(n, m, blocks, detours)
        else:
            self.goal = (n - 1, m - 1)
            self.complete_paths = self.find_paths(n, m, blocks, detours)
            self.num_paths = len(self.complete_paths)

    @staticmethod
    def quick_count(n, m, blocks, detours):
        """
            Counts all total number of paths through the m by n
            grid that don't pass through the points in the blocks
            list and take detours if a point in detours is reached
        """
        def nCr(n, r):
            """
                function that calculates n choose r
            """
            return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

        def count_blocked_paths(x, y, n, m):
            """
                counts paths on n by m grid that travel
                through point x,y
            """
            to_point = nCr(x + y, y)
            from_point = nCr(n - 1 - x + m - 1 - y, n - 1 - x)
            return to_point * from_point

        def count_detour_paths(p1, p2, n, m):
            """
                counts all possible paths to that take the detour
                from p1 to p2. and since p1 to goal is no longer 
                reachable, it adds that to blocked paths list to
                be removed
            """
            if p1 not in blocks:
                blocked = count_blocked_paths(p1[0], p1[1], n, m)
                to_point = nCr(p1[0] + p1[1], p1[1])
                from_point = nCr(n - 1 - p2[0] + m - 1 - p2[1], m - 1 - p2[1])
                blocks.append(p1)
                return to_point * from_point

        total = nCr(n + m - 2, n - 1)
        for d in detours:
            total += count_detour_paths(d[0], d[1], n, m)
        for i in blocks:
            total -= count_blocked_paths(i[0], i[1], n, m)
        return total

    @staticmethod
    def find_paths(n, m, blocks, detours):
        """
            defines a list of active paths, and adds the first seed path
            at 0,0. Runs through while active paths still exist
            checking to see if they are at the goal or can move
            closer to it. Once all active paths terminate, complete
            paths are return
        """
        complete_paths = []
        goal = (n - 1, m - 1)
        seed = Path((0, 0), [], blocks, detours, goal)
        active = [seed]

        while len(active) > 0:
            temp = []
            while len(active) > 0:
                current = active.pop()
                if current.is_goal():
                    complete_paths.append(str(current))
                else:
                    for m in [(0, 1), (1, 0)]:
                        if current.can_move(m):
                            new_coords = (current.coords[0] + m[0], current.coords[1] + m[1])
                            temp.append(Path(new_coords, current.history, blocks, detours, goal))
            active = temp.copy()
        return complete_paths

    def number_of_paths(self):
        """
            number of complete paths through
            the n by m grid
        """
        return self.num_paths

    @property
    def get_paths(self):
        """
            Returns a comma separated list
            of all paths through the grid.
        """
        if self.goal[0] * self.goal[1] >= 40:
            return "Grid too large to find all paths"

        all_paths = ""
        for p in self.complete_paths:
            all_paths += p + ','
        return all_paths[:-1]


class Path:
    """
        Path class represents a path through an n by m
        grid. Each path object has a current (x,y) coordinate,
        a history of all the coordinates its traveled to, a list
        of blocked coordinates, a list of detours (jumps) 
        from point a to point b, and of course, the goal
        coordinate. 
    """

    def __init__(self, coords, history, blocks, detours, goal):
        """
            Initializes a Path obj by checking for immediate
            detours that need to be taken and then sets
            instance variables
        """
        self.goal = goal
        self.blocks = blocks
        self.coords = coords
        self.history = history.copy()
        self.history += [coords]

        for dtr in detours:
            start = dtr[0]
            end = dtr[1]
            if coords == start:
                self.coords = end
                self.history += [end]

    def can_move(self, direction):
        """
            Checks to see if the current path obj
            can move in that direction. Checks if
            the point is blocked or out of grid
            bounds.
        """
        dx = direction[0] + self.coords[0]
        dy = direction[1] + self.coords[1]
        point = (dx, dy)

        for blocked_point in self.blocks:
            if point == blocked_point:
                return False

        if dx < 0 or dx > self.goal[0] or dy < 0 or dy > self.goal[1]:
            return False
        return True

    def is_goal(self):
        """
            Checks to see if the point is at the
            goal coordinates.
        """
        return self.coords[0] == self.goal[0] \
            and self.coords[1] == self.goal[1]

    def __str__(self):
        return str(self.history)

    def __repr__(self):
        return str(self.history)
