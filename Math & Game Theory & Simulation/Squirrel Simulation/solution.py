class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        s = 0
        for nut in nuts:
            s += abs(tree[0] - nut[0]) + abs(tree[1] - nut[1])
        # each nut we need to go from tree to nut then from nut to tree
        s *= 2
       
        result = math.inf
        for nut in nuts:
             # there will only be 1 nut, we will go from sqirrel to nut then nut to tree
            result = min(result, \
            s - abs(tree[0] - nut[0]) - abs(tree[1] - nut[1]) + abs(squirrel[0] - nut[0]) + abs(squirrel[1] - nut[1]))

            
        return result
