class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_pos = (hour * (360/12) + minutes * (360/60/12)) % 360
        min_pos = minutes * (360/60)
        d = max(hour_pos, min_pos) - min(hour_pos, min_pos)
        return min(360-d, d)
