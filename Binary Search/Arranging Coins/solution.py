class Solution:
    def arrangeCoins(self, n: int) -> int:
        start = 0
        end = n
        while start < end:
            mid = start + ceil((end - start + 1) / 2)
            if mid * (mid+1) / 2 > n:
                end = mid - 1
            else:
                start = mid
        return start