class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        start = 0
        end = min(time) * totalTrips
        while start< end:
            mid = start + (end - start) // 2
            trips = 0
            for t in time:
                trips += mid // t
            if trips >= totalTrips:
                end = mid
            else:
                start = mid + 1
        return start
