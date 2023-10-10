class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        s = sorted(set(nums))
        result = math.inf
        j = 0
        for i, mn in enumerate(s):
            mx = mn + n - 1
            while j < len(s) and s[j] <= mx:
                j += 1
            result = min(result, n - (j - i))
        return result
        
