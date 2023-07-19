class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = intervals[0][0] - 1
        result = 0
        for s, e in intervals:
            if s < prev:
                result += 1
                prev = min(prev, e)
            else:
                prev = e
        return result
