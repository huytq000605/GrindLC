from typing import List
from functools import lru_cache


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, k, inTrans):
            if i >= len(prices) or (k == 0 and not inTrans):
                return 0
            result = 0
            if inTrans:
                result = prices[i] + dfs(i + 1, k, False)
            else:
                result = -prices[i] + dfs(i + 1, k - 1, True)
            leave = dfs(i + 1, k, inTrans)
            result = max(result, leave)
            return result
        return dfs(0, k, False)