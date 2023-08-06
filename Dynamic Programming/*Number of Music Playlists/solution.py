class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9 + 7
        @cache
        def dfs(i, used):
            if i == goal:
                if used == n:
                    return 1
                return 0
            # choose new song
            result = dfs(i+1, used + 1) * (n-used)
            result %= MOD
            
            # repeat song
            if used >= k:
                result += dfs(i+1, used) * (used - k)
                result %= MOD
            # dp[i][j] = dp[i+1][j+1] * (n-j) + dp[i+1][j] * (j - k)
            return result
        
        return dfs(0, 0)
