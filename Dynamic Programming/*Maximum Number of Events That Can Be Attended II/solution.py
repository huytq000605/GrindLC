from functools import cache


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key = lambda event: event[0])
        
        @cache
        def dfs(idx, k):
            if k == 0 or idx >= len(events):
                return 0
            leaveEvent = dfs(idx + 1, k)
            start = idx
            end = len(events) - 1
            while start < end:
                mid = start + (end - start) // 2
                if events[mid][0] <= events[idx][1]:
                    start = mid + 1
                else:
                    end = mid
            nextIdx = start
            if events[nextIdx][0] <= events[idx][1]:
                nextIdx += 1
            joinEvent = dfs(nextIdx, k - 1) + events[idx][2]
            return max(joinEvent, leaveEvent)
        
        return dfs(0, k)