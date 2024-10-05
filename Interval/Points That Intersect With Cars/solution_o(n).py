class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        lines = [0 for _ in range(100+1)]
        for s, e in nums:
            lines[s-1] += 1
            lines[e] -= 1
        result = 0
        intervals = 0
        for p in lines:
            intervals += p
            if intervals: result += 1
        return result
