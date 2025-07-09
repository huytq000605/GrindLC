class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        events = [(startTime[i], endTime[i]) for i in range(n)]
        events.sort()
        prev = 0
        free = 0
        result = 0
        times = deque([])
        for i in range(n):
            s, e = events[i]
            free += s - prev
            times.append(s - prev)
            result = max(result, free)
            prev = e
            if len(times) == k+1: free -= times.popleft()
        result = max(result, free + eventTime - prev)
        return result
