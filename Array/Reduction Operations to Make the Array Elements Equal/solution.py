class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        result = 0
        cur = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] < nums[i-1]:
                result += cur
            cur += 1
        return result
