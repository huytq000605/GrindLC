class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        target = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] + 1 != nums[i]:
                break
            target += nums[i]
        s = set(nums)
        while target in s:
            target += 1
        return target
