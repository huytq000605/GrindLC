import math

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        max_num = max(nums)
        min_num = min(nums)
        if max_num == min_num:
            return 0
        each_bucket = math.ceil((max_num - min_num) / (n-1))
        max_buckets = [-1 for i in range(n)]
        min_buckets = [math.inf for i in range(n)]
        
        for num in nums:
            index = (num - min_num) // each_bucket
            max_buckets[index] = max(max_buckets[index], num)
            min_buckets[index] = min(min_buckets[index], num)
        result = 0
        prev = -1
        for i in range(n):
            if max_buckets[i] == -1:
                continue
            if prev != -1:
                result = max(result, min_buckets[i] - prev)
            prev = max_buckets[i]
        return result