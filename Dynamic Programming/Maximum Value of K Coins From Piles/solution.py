class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        # dfs(i, k) have (k+1) transactions till the end => Time complexity: len(piles) * k 
        @cache
        def dfs(i, k):
            if i >= n: return 0
            value = 0
            m = len(piles[i])
            result = 0
            for coins in range(min(k, m) + 1):
                if coins > 0:
                    value += piles[i][coins-1]
                result = max(result, value + dfs(i + 1, k - coins))
            return result
        return dfs(0, k)
