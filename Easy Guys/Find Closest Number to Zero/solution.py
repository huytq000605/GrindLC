class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        result = 10**9
        min_diff = 10**9
        for num in nums:
            diff = abs(num)
            if diff < min_diff:
                min_diff = diff
                result = num
            elif diff == min_diff:
                result = max(result, num)
        return result