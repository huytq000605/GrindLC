class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()
        groups = 0
        last_end = -1
        for s, e in ranges:
            if s > last_end:
                groups += 1
            last_end = max(last_end, e)
        return pow(2, groups, 10**9 + 7)
