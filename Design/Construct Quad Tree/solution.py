"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def value(r1, r2, c1, c2):
            val = grid[r1][c1]
            for r in range(r1, r2+1):
                for c in range(c1, c2+1):
                    if grid[r][c] != val:
                        return -1
            return val
                    
        def build(r1, r2, c1, c2):
            val = value(r1, r2, c1, c2)
            if val != -1:
                return Node(val, True, None, None, None, None)
            mr = r1 + (r2 - r1) // 2
            mc = c1 + (c2 - c1) // 2
            return Node(1, False,\
                       build(r1, mr, c1, mc), build(r1, mr, mc+1, c2), \
                       build(mr+1, r2, c1, mc), build(mr+1, r2, mc+1, c2) \
                       )
        return build(0, len(grid) - 1, 0, len(grid[0]) - 1)
                    
