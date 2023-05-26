class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0 for _ in range(n)]
        for i in range(n):
            if i > 0:
                prefix[i] = prefix[i-1]
            prefix[i] |= nums[i]
        
        suffix = [0 for _ in range(n)]
        for i in reversed(range(n)):
            if i < n-1:
                suffix[i] = suffix[i+1]
            suffix[i] |= nums[i]
        
        result = 0
        for i, num in enumerate(nums):
            left, right = 0, 0
            if i > 0: left = prefix[i-1]
            if i < n-1: right = suffix[i+1]
            result = max(result, left | right | (num << k))
        return result
