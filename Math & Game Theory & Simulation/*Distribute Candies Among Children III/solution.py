class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # **|*|**
        # stars + 2 places to place 2 bars
        def ways(stars):
            if stars < 0: return 0
            return comb(stars+2, 2)
        result = ways(n)
        # Inclusion-exlucsion principle
        over_limit = limit + 1
        result -= 3*ways(n-over_limit)
        result += 3*ways(n - 2 * over_limit)
        result -= ways(n - 3 * over_limit)
        return result
