class Solution:
    def numberOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        # dp[i] = number of ways for i*2 people
        dp = [0 for _ in range(n//2+1)]
        dp[0] = 1
        for i in range(1, n//2+1):
            for j in range(i):
                dp[i] = (dp[i] + dp[j] * dp[i-1-j]) % MOD
        return dp[-1]
        


class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        MOD = 10**9 + 7
        @cache
        def dfs(n):
            if n <= 2: return 1
            result = 0
            for i in range(0, n-2+1, 2):
                result += dfs(i) * dfs(n-2-i)
            return result % MOD
        return dfs(numPeople)
