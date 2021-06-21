from typing import List, Tuple
from functools import lru_cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @lru_cache(maxsize = None)
        def helper(amount: int, coins: Tuple) -> int:
            if amount == 0:
                return 1
            if amount < 0 or len(coins) == 0:
                return 0
            return helper(amount - coins[-1], coins) + helper(amount, coins[0:-1])
        return helper(amount, tuple(coins))
        