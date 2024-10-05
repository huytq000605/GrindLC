class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        result = set()
        for s, e in nums:
            for i in range(s, e + 1):
                result.add(i)
        return len(result)
