class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour <= len(dist) - 1:
            return -1

        def valid(speed):
            take = 0
            for d in dist:
                if take + d / speed > hour: return False
                take += math.ceil(d / speed)
            return True
        
        start = 1
        end = 10**7
        while start < end:
            mid = start + (end - start) // 2
            if valid(mid):
                end = mid
            else:
                start = mid + 1
        return start
