class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        s = 0
        n = len(nums)
        result = math.inf
        seen = dict()
        seen[0] = -1
        for i, num in enumerate(nums):
            s += num
            if s not in seen:
                seen[s] = i
            if s - target in seen:
                result = min(result, n - (i - seen[s - target]))
        if result == math.inf:
            return -1
        return result
                
