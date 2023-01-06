class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        pq = []
        for start, end in intervals:
            if not pq or pq[0] >= start:
                heappush(pq, end)
            else:
                heappop(pq)
                heappush(pq, end)
        return len(pq)
