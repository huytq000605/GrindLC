class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        mn = (nums[0], 0)
        mx = (nums[0], 0)
        for i in range(indexDifference, len(nums)):
            if nums[i - indexDifference] < mn[0]:
                mn = [nums[i - indexDifference], i - indexDifference]
            if nums[i - indexDifference] > mx[0]:
                mx = [nums[i - indexDifference], i - indexDifference]
            if abs(nums[i] - mn[0]) >= valueDifference:
                return [i, mn[1]]
            if abs(nums[i] - mx[0]) >= valueDifference:
                return [i, mx[1]]
            
        return [-1, -1]
