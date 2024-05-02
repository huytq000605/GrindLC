class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set()
        result = -1
        for num in nums:
            s.add(num)
            if num in s and -num in s:
                result = max(result, abs(num))
        return result
