class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [0 for _ in range(m+1)]
        for i in range(n-1, -1, -1):
            next_dp = [0 for _ in range(m+1)]
            for j in range(m-1, -1, -1):
                if text2[i] == text1[j]:
                    next_dp[j] = 1 + dp[j+1]
                next_dp[j] = max(next_dp[j], next_dp[j+1], dp[j])
            dp = next_dp
        return dp[0]
        # if t1[i] == t2[j]
        # dp[i][j] = dp[i+1][j+1]
        # dp[i][j] = max(dp[i+1][j], dp[i][j+1])
       
