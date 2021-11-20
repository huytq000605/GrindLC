class Solution:
	# Increase n-1 element except the max => Decrease the max by 1
	# The problem become decrease each number to the minNumber
    def minMoves(self, nums: List[int]) -> int:
        minNum = nums[0]
        minNum = min(minNum, *nums)
        result = 0
        for num in nums:
            result += num - minNum
        return result