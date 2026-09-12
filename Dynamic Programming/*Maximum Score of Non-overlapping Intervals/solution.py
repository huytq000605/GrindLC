class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        idxs = dict()
        for i, (u, v, w) in enumerate(intervals):
            if (u, v, w) not in idxs:
                idxs[(u, v, w)] = i
        intervals = sorted(idxs.keys(), key = lambda x: x[1])
        n = len(intervals)
        dp = [(0, []) for _ in range(n+1)]
        for _ in range(4):
            ndp = [(0, []) for _ in range(n+1)]
            for i in range(n):
                u, v, w = intervals[i]
                j = bisect_left(intervals, u, key = lambda x: x[1])
                ndp[i+1] = min(ndp[i], (dp[j][0]-w, sorted(dp[j][1] + [idxs[(u, v, w)]])))
            dp = ndp
        return dp[-1][1]
""" Top down
class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        idxs = dict()
        for i, (u, v, w) in enumerate(intervals):
            if (u, v, w) not in idxs:
                idxs[(u, v, w)] = i
        intervals = sorted(idxs.keys())
        n = len(intervals)
        @cache
        def dfs(i, k):
            if i >= n or k == 0: return [0, []]
            skip = dfs(i+1, k)
            j = bisect_right(intervals, (intervals[i][1], math.inf, math.inf))
            ret_pick = dfs(j, k-1)
            pick = [ret_pick[0]-intervals[i][2], sorted([*ret_pick[1], idxs[intervals[i]]]) ]
            return min(pick, skip)

        return dfs(0, 4)[1]
        
"""
