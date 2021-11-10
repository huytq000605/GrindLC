class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        numOfNumber = 0
        result = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] != nums[i - 1]:
                result += numOfNumber
            numOfNumber += 1
        return result
                