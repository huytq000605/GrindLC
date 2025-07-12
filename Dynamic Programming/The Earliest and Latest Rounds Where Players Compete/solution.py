class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        mn, mx = math.inf, -math.inf
        firstPlayer -= 1
        secondPlayer -= 1
        @cache
        def dfs(mask, i, j, r):
            nonlocal mn, mx
            if i >= j:
                dfs(mask, 0, n-1, r+1)
            elif (mask & (1 << i)) == 0:
                dfs(mask, i+1, j, r)
            elif (mask & (1 << j)) == 0:
                dfs(mask, i, j-1, r)
            elif i == firstPlayer and j == secondPlayer:
                mn = min(mn, r)
                mx = max(mx, r)
            else:
                if i != firstPlayer and i != secondPlayer:
                    dfs(mask ^ (1 << i), i+1, j-1, r)
                if j != firstPlayer and j != secondPlayer:
                    dfs(mask ^ (1 << j), i+1, j-1, r)
        dfs((1<<n)-1, 0, n-1, 1)
        dfs.cache_clear()
        return [mn, mx]
