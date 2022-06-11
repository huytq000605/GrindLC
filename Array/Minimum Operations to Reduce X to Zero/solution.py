class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        if x == 0:
            return 0
        target = sum(nums) - x
        seen = dict()
        seen[0] = -1
        result = n+1
        total = 0
        for i, num in enumerate(nums):
            total += num
            if total not in seen:
                seen[total] = i
            if total - target in seen:
                result = min(result, n - (i - seen[total - target]))
        if result > n:
            return -1
        return result
