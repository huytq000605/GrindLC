class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [0 for i in range(target + 1)]
        for d, c in enumerate(cost):
            d = d + 1
            if c >= len(dp):
                continue
            dp[c] = max(dp[c], d)
            
        for i in range(target + 1):
            for d, c in enumerate(cost):
                d = d + 1
                if i < c or dp[i-c] == 0:
                    continue
                dp[i] = max(dp[i], dp[i-c]*10 + d)
        return str(dp[-1])