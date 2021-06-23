from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        numOfBlank = {}
        maxBlank = 0
        for row in wall:
            col = 0
            for brick in row:
                if col != 0:
                    if numOfBlank.get(col) == None:
                        numOfBlank[col] = 0
                    numOfBlank[col]+= 1
                    maxBlank = max(maxBlank, numOfBlank[col])
                col += brick
            
        return len(wall) - maxBlank