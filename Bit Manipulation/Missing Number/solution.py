class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append(-1)
        n = len(nums)
        for i in range(n):
            while nums[i] != i and nums[i] >= 0:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        for i in range(n):
            if nums[i] != i:
                return i
        return -1