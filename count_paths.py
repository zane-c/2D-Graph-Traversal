import math


def count_paths(n, m, blocks, detours):
    def nCr(n, r):
        return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

    def count_blocked_paths(x, y, n, m):
        toP = nCr(x + y, y)
        fromP = nCr(n-1-x + m-1-y, n-1-x)
        return toP * fromP

    def count_detour_paths(p1, p2, n, m):
        blocked = count_blocked_paths(p1[0], p1[1], n, m)
        toP = nCr(p1[0] + p1[1], p1[1])
        fromP = nCr(n-1-p2[0] + m-1-p2[1], m-1-p2[1])
        print(toP, fromP, blocked)
        return toP * fromP - blocked

    blocks = set(blocks)
    detours = set(detours)

    total = nCr(n+m-2, n-1)
    
    for i in blocks:
        total -= count_blocked_paths(i[0], i[1], n, m)

    for d in detours:
        remove =  count_detour_paths(d[0], d[1], n, m)
        print(remove)
        total += remove

    print(total)
