class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = []
        for i, r in enumerate(ranges):
            intervals.append((max(i-r, 0), min(i+r, n)))
        intervals.sort()
        
        @cache
        def dfs(idx, last):
            if idx >= len(intervals):
                if last == n:
                    return 0
                return math.inf
            if last < intervals[idx][0]:
                return math.inf
            take_this = 1 + dfs(idx + 1, max(last, intervals[idx][1]))
            ignore_this = dfs(idx + 1, last)
            return min(take_this, ignore_this)
        
        result = dfs(0, 0)
        if result == math.inf:
            return -1
        return result