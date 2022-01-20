class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        start = 1
        end = max(piles)
        while start < end:
            mid = start + (end - start) // 2
            time = 0
            for pile in piles:
                time += ceil(pile / mid)
            if time <= h:
                end = mid
            else:
                start = mid + 1
        return start