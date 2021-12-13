from functools import cache
import math
from typing import *

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(states):
            if states == (1 << n) - 1:
                return 0
            i = 0
            for j in range(n):
                i += (states >> j) & 1
            i = i // 2 + 1
            result = 0
            for j in range(n):
                if (states >> j) & 1 == 1:
                    continue
                for k in range(j + 1, n):
                    if (states >> k) & 1 == 1:
                        continue
                    nextStates = states | (1 << j) | (1 << k)
                    result = max(result, i * math.gcd(nums[j], nums[k]) + dfs(nextStates))
            return result
        return dfs(0)