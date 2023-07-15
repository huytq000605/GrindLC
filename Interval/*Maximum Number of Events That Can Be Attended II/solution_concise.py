class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        starts = [event[0] for event in events]
        @cache
        def dfs(i, k):
            if i >= len(events) or k <= 0:
                return 0
            start, end, value = events[i]
            next_idx = bisect.bisect_left(starts, end + 1)
            take = value + dfs(next_idx, k-1)
            skip = dfs(i + 1, k)
            return max(take, skip)
        return dfs(0, k)
