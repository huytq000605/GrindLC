class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        last = [-1 for i in range(30)]
        n = len(nums)
        result = [1 for i in range(n)]
        for i in range(n-1, -1, -1):
            num = nums[i]
            for j in range(30):
                if (num >> j) & 1:
                    last[j] = i
                result[i] = max(result[i], last[j] - i + 1)
        return result
