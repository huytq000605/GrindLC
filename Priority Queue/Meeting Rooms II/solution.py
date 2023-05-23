class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        pq = []
        result = 0
        for s, e in intervals:
            while pq and pq[0] <= s:
                heappop(pq)
            heappush(pq, e)
            result = max(result, len(pq))
        return result
