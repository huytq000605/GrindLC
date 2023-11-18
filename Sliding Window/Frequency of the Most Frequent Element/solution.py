class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        start = 0
        result = 0
        s = 0
        for i, num in enumerate(nums):
            s += num
            while num * (i - start + 1) - s > k:
                s -= nums[start]
                start += 1
            result = max(result, i - start + 1)
        return result
