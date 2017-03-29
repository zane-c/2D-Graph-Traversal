n = 5
m = 5
blocked = [(2, 1)]
#blocked = []
#jumps = [((2,1),(0,3))]
jumps = []

class Node:

    def __init__(self, coords, history, goal): 
        for j in jumps:
            start = j[0]
            end = j[1]
            if coords == start:
                coords = end

        self.goal = goal
        self.coords = coords
        self.history = history.copy()
        self.history += [coords]

    def can_move(self, direction):
        dx = direction[0] + self.coords[0]
        dy = direction[1] + self.coords[1]
        point = (dx, dy)

        for blocked_point in blocked:
            if point == blocked_point:
                return False

        if dx < 0 or dx > self.goal[0] or dy < 0 or dy > self.goal[1]:
            return False
        return True

    def is_goal(self):
        return self.coords[0] == self.goal[0] \
               and self.coords[1] == self.goal[1]

    def __str__(self):
        return str(self.history)

    def __repr__(self):
        return str(self.history)


class PathFinder:

    moves = [(0,1), (1,0)]
    dead = []
    alive = [Node((0,0), [], goal)]

    def __init__(self, n, m, )




    
goal = (n-1,m-1)
moves = [(0,1), (1,0)]
paths = []
alive = [Node((0,0), [], goal)]



while len(alive) > 0:

    temp = []
    while len(alive) > 0:

        cur_node = alive.pop()
        if cur_node.is_goal():
            paths.append(str(cur_node))
        else:
            for m in moves:
                if cur_node.can_move(m):
                    new_coords = (cur_node.coords[0] + m[0], cur_node.coords[1] + m[1])
                    temp.append(Node(new_coords, cur_node.history, goal))

    alive = temp.copy()
            

for p in paths:
    print(p)
print(len(paths))
