class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda interval: (interval[0], -interval[1]))
        result = 0
        cur_end = -1
        for s, e in intervals:
            if s > cur_end or e > cur_end:
                result += 1
            cur_end = max(cur_end, e)
        return result