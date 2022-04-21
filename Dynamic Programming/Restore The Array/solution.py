class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        dp = [0 for i in range(len(s) + 1)] # dp[i] number of Array where build s have i first elements
        dp[0] = 1 # 0 element => 1 way
        for i in range(1, len(s) + 1):
            for distance in range(len(str(k))):
                start = i - distance - 1 # Get the idx where num starts
                if start < 0: # out of range
                    break
                if s[start] == "0":
                    continue
                num = int(s[start:i])
                if num > k:
                    break
                dp[i] += dp[start]
                dp[i] %= (10**9+7)
        return dp[-1]