class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        # dfs(i, k) have (k+1) transactions till the end => Time complexity: len(piles) * k 
        @cache
        def dfs(i, k):
            if k == 0 or i >= len(piles):
                return 0
            result = 0
            score = 0
            for coins in range(min(len(piles[i]) + 1, k + 1)):
                if coins > 0:
                    score += piles[i][coins - 1]
                result = max(result, score + dfs(i + 1, k - coins))
            return result
        return dfs(0, k)