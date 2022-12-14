class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev1, prev2 = 0, 0
        for num in nums:
            cur = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = cur
        return max(prev1, prev2)
