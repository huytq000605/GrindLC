from functools import lru_cache
import math

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0, *cuts, n]

        @lru_cache(None)
        def dfs(start, end):
            if start + 1 >= end:
                return 0
            result = math.inf
            for cut in range(start + 1, end):
                result = min(result, cuts[end] - cuts[start] + dfs(start, cut) + dfs(cut, end))
            return result
        return dfs(0, len(cuts) - 1)