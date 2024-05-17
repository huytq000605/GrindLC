## BOTTOM UP
class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        # dp[i] = 1 + dp[j-1] for j in range(i, -1, -1) and condition
        dp = [math.inf for _ in range(len(s) + 1)]
        dp[0] = 0
        for i in range(len(s)):
            counter = Counter()
            n = 0
            mx = 0
            for j in range(i, -1, -1):
                counter[s[j]] += 1
                mx = max(mx, counter[s[j]])
                n += 1
                if mx * len(counter) == n:
                    dp[i+1] = min(dp[i+1], 1 + dp[j])
        return dp[-1]

## TOP DOWN
class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        @cache
        def dfs(i):
            if i < 0: return 0
            counter = Counter()
            result = math.inf
            mx = 0
            n = 0
            for j in range(i, -1, -1):
                counter[s[j]] += 1
                mx = max(mx, counter[s[j]])
                n += 1
                if mx * len(counter) == n:
                    result = min(result, 1+dfs(j-1))
            return result
        return dfs(len(s) - 1)
