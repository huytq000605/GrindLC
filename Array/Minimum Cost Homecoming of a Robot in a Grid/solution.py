class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        result = 0
                
        left = min(startPos[0], homePos[0])
        right = max(startPos[0], homePos[0])
        for i in range(left, right + 1):
            result += rowCosts[i]
        
        up = min(startPos[1], homePos[1])
        down = max(startPos[1], homePos[1])
        for i in range(up, down + 1):
            result += colCosts[i]
        
        result -= rowCosts[startPos[0]]
        result -= colCosts[startPos[1]]
        return result 