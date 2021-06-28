from functools import lru_cache
from typing import List

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @lru_cache(None)
        def helper(start, end):
            if end - start + 1 < 3:
                return 0
            result = float("inf")
            for i in range(start + 1, end):
                result = min(result, values[start]*values[end]*values[i] + helper(start, i) + helper(i , end))
            return result
        return helper(0, len(values) - 1)