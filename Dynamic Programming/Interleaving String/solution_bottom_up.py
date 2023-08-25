class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, p = len(s1), len(s2), len(s3)
        if m + n != p:
            return False
        # dp[i][j]
        # if s1[i] == s3[i+j]: dp[i][j] = dp[i+1][j]
        # if s2[j] == s3[i+j]: dp[i][j] = dp[i][j] or dp[i][j+1]
        dp = [[False for j in range(n + 1)] for i in range(m + 1)]
        dp[-1][-1] = True
        
        for i in reversed(range(m+1)):
            for j in reversed(range(n+1)):
                if i < m and dp[i+1][j] and s1[i] == s3[i+j]: dp[i][j] = True
                if j < n and dp[i][j+1] and s2[j] == s3[i+j]: dp[i][j] = True
        
        return dp[0][0]
