import itertools, math
from functools import cache
from typing import *

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        each = n // k
        nums.sort()
        @cache
        def dfs(nums):
            if len(nums) == 0:
                return 0
            result = math.inf
            for elements in itertools.combinations(nums, each):
                if len(set(elements)) != each:
                    continue
                new_nums = list(nums)
                for num in elements:
                    new_nums.remove(num)
                new_nums.sort()
                result = min(result, max(elements) - min(elements) + dfs(tuple(new_nums)))
            return result
        result = dfs(tuple(nums))
        if result >= math.inf:
            return -1
        return result