class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                dp[l][r] = 1
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                dp[l][r] = 1
                l -= 1
                r += 1
        
        result = 0
        for i in range(n):
            for j in range(i, n):
                result += dp[i][j]
        return result
