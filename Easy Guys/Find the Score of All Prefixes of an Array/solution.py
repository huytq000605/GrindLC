class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0 for _ in range(n)]
        mx = 0
        for i, num in enumerate(nums):
            if i > 0:
                result[i] = result[i-1]
            mx = max(mx, num)
            result[i] += num + mx
        return result
