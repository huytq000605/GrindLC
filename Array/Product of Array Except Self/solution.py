class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1 for _ in range(n)]
        cur = 1
        for i in range(n):
            result[i] *= cur
            cur *= nums[i]
        cur = 1
        for i in reversed(range(n)):
            result[i] *= cur
            cur *= nums[i]
        return result

