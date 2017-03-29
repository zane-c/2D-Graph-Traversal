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


class PathFinder:
    """
        The path finder class finds all possible solution
        paths through an n by m grid that might or might
        not have blocked paths or detours.
    """

    def __init__(self, n, m, blocks, detours):
        """
            Initializes instance variables and then
            calls find_solution
        """
        self.blocks = blocks
        self.detours = detours
        self.goal = (n-1, m-1)
        self.complete_paths = []
        self.num_paths = 0
        self.find_solution()

    def find_solution(self):
        """
            defines a list of active paths (paths that are not
            complete or dead end), and adds the first seed path
            at 0,0. Runs through while active paths still exist
            checking to see if they are at the goal or can move
            closer to it. Once all active paths terminate, results
            are logged for later use in below functions.
        """
        seed = Path((0, 0), [], self.blocks, self.detours, self.goal)
        active = [seed]

        while len(active) > 0:
            temp = []
            while len(active) > 0:
                current = active.pop()
                if current.is_goal():
                    self.complete_paths.append(str(current))
                else:
                    for m in [(0, 1), (1, 0)]:
                        if current.can_move(m):
                            new_coords = (current.coords[0] + m[0], current.coords[1] + m[1])
                            temp.append(Path(new_coords, current.history, self.blocks, self.detours, self.goal))
            active = temp.copy()
        self.num_paths = len(self.complete_paths)
    
    def number_of_paths(self):
        """
            number of complete paths through
            the n by m grid
        """
        return self.num_paths

    def get_paths(self):
        """
            Returns a comma separated list
            of all paths through the grid.
        """
        all_paths = ""
        for p in self.complete_paths:
            all_paths += p + ','
        return all_paths[:-1]
