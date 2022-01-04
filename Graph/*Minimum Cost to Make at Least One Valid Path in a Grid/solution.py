from typing import *
from heapq import heappush, heappop
import math

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        queue = [[0, 0, 0]]
        dirCell = [[0,0], [0, 1], [0, -1], [1, 0], [-1, 0]]
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        distance = [math.inf for i in range(len(grid) * len(grid[0]))]
        distance[0] = 0
        
        def getIdx(i, j):
            return i * len(grid[0]) + j
        
        while len(queue):
            curCost, i, j = heappop(queue)
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return curCost
            cell = grid[i][j]
            for d in dirs:
                cost = 1
                if dirCell[cell][0] == d[0] and dirCell[cell][1] == d[1]:
                    cost = 0
                ni, nj = i + d[0], j + d[1]
                if ni < 0 or ni >= len(grid) or nj < 0 or nj >= len(grid[0]): continue
                if distance[getIdx(ni, nj)] > curCost + cost:
                    distance[getIdx(ni, nj)] = curCost + cost
                    heappush(queue, [curCost + cost, ni, nj])
        return -1
        