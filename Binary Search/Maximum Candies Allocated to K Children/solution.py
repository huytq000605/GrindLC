class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        start = 0
        candies = sorted(candies, reverse = True)
        end = sum(candies) // k
        while start < end:
            c = 0
            mid = start + math.ceil((end - start + 1) / 2)
            for candy in candies:
                if candy < mid:
                    break
                c += candy // mid
            if c >= k:
                start = mid
            else:
                end = mid - 1
        return start