class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        d = set(dictionary)
        # how many characters are left if we use first `i` characters
        dp = [0 for _ in range(n+1)]
        for i in range(n):
            dp[i+1] = dp[i] + 1
            for j in range(i+1):
                if s[j:i+1] in d:
                    dp[i+1] = min(dp[i+1], dp[j])
        return dp[n]
