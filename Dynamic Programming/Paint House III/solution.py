from typing import *
from functools import cache
import math

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @cache
        def dfs(idx, group, prev):
            if group > target:
                return math.inf
            if idx >= m:
                if group != target:
                    return math.inf
                return 0
            if houses[idx] > 0:
                if houses[idx] == prev:
                    return dfs(idx + 1, group, houses[idx])
                else:
                    return dfs(idx + 1, group + 1, houses[idx])
            result = math.inf
            if group < target:
                for i in range(n):
                    color = i + 1
                    if color == prev:
                        result = min(result, cost[idx][color - 1] + dfs(idx + 1, group, prev))
                    else:
                        result = min(result, cost[idx][color - 1] + dfs(idx + 1, group + 1, color))
            else:
                result = cost[idx][prev - 1] + dfs(idx + 1, group, prev)
            return result
        
        result = dfs(0, 0, -1)
        if result == math.inf:
            return -1
        return result
                    