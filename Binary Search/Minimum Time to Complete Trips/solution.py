class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        time.sort()
        start = 0
        end = 10**7 * 10**7
        while start < end:
            mid = start + (end - start) // 2
            trips = 0
            for t in time:
                if t > mid:
                    break
                trips += mid // t
            if trips >= totalTrips:
                end = mid
            else:
                start = mid + 1
        return start