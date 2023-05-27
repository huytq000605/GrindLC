class Solution:
    def stoneGameIII(self, piles: List[int]) -> str:
        n = len(piles)
        @cache
        def dfs(i):
            if i >= n:
                return 0
            s = 0
            result = -math.inf
            for ni in range(i, min(n, i + 3)):
                s += piles[ni]
                result = max(result, s - dfs(ni+1))
            return result
        diff = dfs(0)
        if diff > 0:
            return "Alice"
        elif diff < 0:
            return "Bob"
        else:
            return "Tie"
