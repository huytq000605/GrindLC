class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        start = 0
        n = len(nums)
        result = 0
        total = 0
        for end in range(n):
            total += nums[end]
            while start <= end and total * (end - start + 1) >= k:
                total -= nums[start]
                start += 1
            result += (end - start + 1)
        return result