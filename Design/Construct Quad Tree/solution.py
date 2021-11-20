# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build(sR, eR, sC, eC):
            if sR == eR:
                return Node(grid[sR][sC], True, None, None, None, None)
            mR = sR + (eR - sR) // 2
            mC = sC + (eC - sC) // 2
            value = grid[sR][sC]
            for i in range(sR, eR + 1):
                for j in range(sC, eC + 1):
                    if grid[i][j] != value:
                        return Node(grid[sR][sC], False, build(sR, mR, sC, mC), build(sR, mR, mC + 1, eC) , build(mR + 1, eR, sC, mC), build(mR+1,eR, mC + 1, eC))
            return Node(grid[sR][sC], True, None, None, None, None)
        return build(0, len(grid) - 1, 0, len(grid) - 1)
                        