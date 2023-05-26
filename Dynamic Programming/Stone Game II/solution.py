class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        @cache
        def dfs(i, m):
            if i >= n:
                return 0
            result = -math.inf
            s = 0
            for j in range(i, min(n, i + 2*m)):
                s += piles[j]
                result = max(result, s - dfs(j+1, max(m, j-i+1)))
            return result

        sub = dfs(0, 1)
        return (sum(piles) + sub)//2
                
