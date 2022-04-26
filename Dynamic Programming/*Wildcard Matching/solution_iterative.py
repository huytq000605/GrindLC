class Solution:
    def isMatch(self, s: str, p: str) -> bool:
				# dp[i][j] is it match for s[:i] and p[:j]
        dp = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(len(p)):
            if p[i] != "*":
                break
            dp[0][i+1] = True
            
        for i in range(len(s)):
            for j in range(len(p)):
                if s[i] == p[j] or p[j] == "?":
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == "*":
                    dp[i+1][j+1] = dp[i][j+1] or dp[i+1][j]
        return dp[len(s)][len(p)]
                