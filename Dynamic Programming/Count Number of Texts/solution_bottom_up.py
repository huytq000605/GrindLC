class Solution:
    def countTexts(self, keys: str) -> int:
        n = len(keys)
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(n):
            for j in range(0, 4):
                if (i-j) < 0 or keys[i-j] != keys[i] or (j == 3 and keys[i] not in ["7", "9"]):
                    break
                dp[i+1] += dp[i-j]
                dp[i+1] %= 10**9 + 7
        return dp[-1]