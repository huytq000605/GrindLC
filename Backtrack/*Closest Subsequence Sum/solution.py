from typing import *
import math
from bisect import bisect_left

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        first = nums[:n//2]
        second = nums[n//2:]
        
        def get_sums(arr):
            sums = set()
            def dfs(idx, current_sum):
                if idx >= len(arr):
                    sums.add(current_sum)
                    return
                dfs(idx + 1, current_sum + arr[idx])
                dfs(idx + 1, current_sum)
            dfs(0, 0)
            return sums
        
        first_sums, second_sums = get_sums(first), get_sums(second)
        second_sums = sorted(second_sums)
        result = math.inf
        for first_sum in first_sums:
            remain = goal - first_sum
            # start = 0
            # end = len(second_sums) - 1
            # while start <= end:
            #     mid = start + (end - start) // 2
            #     result = min(result, abs(remain - second_sums[mid]))
            #     if second_sums[mid] <= remain:
            #         start = mid + 1
            #     else:
            #         end = mid - 1
            i2=bisect_left(second_sums,remain)
            if i2<len(second_sums):
                    result=min(result,abs(remain-second_sums[i2]))
            if i2>0:
                    result=min(result,abs(remain-second_sums[i2-1]))
        return result