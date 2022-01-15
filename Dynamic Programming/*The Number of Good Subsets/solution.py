from typing import *
from functools import cache
import math

class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        result = 0
        freq_nums = Counter()
        not_good = {4, 8, 9, 12, 16, 18, 20, 24, 25, 27, 28}
        for idx, num in enumerate(nums):
            if num in not_good:
                continue
            freq_nums[num] += 1

        nums = sorted(list(freq_nums.keys()), reverse = True) 
        n = len(nums)

        @cache
        def dfs(idx, mask):
            current_num = 1
            for i in range(idx):
                if (mask & (1 << i)) != 0:
                    current_num *= nums[i]
            if idx >= len(nums):
                if current_num == 1:
                    return 0
                return 1
            result = 0
            if math.gcd(current_num, nums[idx]) == 1:
                result += freq_nums[nums[idx]] * dfs(idx + 1, mask | (1 << idx))
            result += dfs(idx + 1, mask)
            return result % (10 ** 9 + 7)
            
        if n == 0:
            return 0
        elif nums[-1] == 1:
            nums.pop()
            result = dfs(0, 0) + ((1 << freq_nums[1]) - 1) * dfs(0, 0)
            return result % (10 ** 9 + 7)
        else:
            return dfs(0, 0)