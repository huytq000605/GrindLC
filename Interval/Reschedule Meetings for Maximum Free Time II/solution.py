class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        events = [(startTime[i], endTime[i]) for i in range(n)]
        events.sort()

        pq = []
        prev = 0
        heappush(pq, eventTime - events[-1][1])
        for i in range(n):
            s, e = events[i]
            heappush(pq, s - prev)
            prev = e
            if len(pq) > 3: heappop(pq)
        pq.sort()

        def valid(m, l, r):
            i = len(pq) - 1
            if i >= 0 and max(l, r) == pq[i]:
                i -= 1
            if i >= 0 and min(l, r) == pq[i]:
                i -= 1
            return i >= 0 and m <= pq[i]

        prev = 0
        result = 0
        for i in range(n):
            s, e = events[i]
            left = s - prev
            right = events[i+1][0] - e if i+1 < n else eventTime - e
            if valid(e-s, left, right):
                result = max(result, e-s+left+right)
            else:
                result = max(result, left + right)
            prev = e

        return result
