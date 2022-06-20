from heapq import heappush, heappop
from typing import *

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        m = len(nums)
        n = m // 3
        first = []
        second = []
        
        for num in nums[:n]:
            heappush(first, -num)
        
        for num in nums[2*n:]:
            heappush(second, num)
            
        sum_first = sum(first)
        sum_second = sum(second)
        
        ori_sum_first = sum_first
        
        prefix_first = [-sum_first for i in range(n+1)]
        prefix_second = [sum_second for i in range(n+1)]
        result = -sum_first - sum_second
        
        middle = nums[n:n*2]
        for i in range(n):
            num = middle[i]
            if num < -first[0]:
                sum_first -= heappop(first)
                sum_first -= num
                heappush(first, -num)
            prefix_first[i] = sum_first
        
        for i in range(n - 1, -1, -1):
            num = middle[i]
            if num > second[0]:
                sum_second -= heappop(second)
                sum_second += num
                heappush(second, num)
            prefix_second[i] = sum_second
        
        for i in range(n):
            result = min(result, -prefix_first[i] - prefix_second[i+1])
        result = min(result, -ori_sum_first - prefix_second[0])
        return result