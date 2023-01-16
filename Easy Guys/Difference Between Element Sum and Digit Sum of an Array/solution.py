class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s = sum(nums)
        ds = 0
        for num in nums:
            while num:
                ds += num % 10
                num //= 10
        return abs(s - ds)
