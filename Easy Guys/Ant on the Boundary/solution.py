class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        result = 0
        p = 0
        for num in nums:
            p += num
            result += p == 0
        return result
