class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # Needs to cover the whole range
        # dp[i] = number of taps to cover all the garden from i backward
        dp = [0] + [math.inf for i in range(n)]
        for i, r in enumerate(ranges):
            left, right = max(0, i - r), min(n, i + r)
            for j in range(left, right + 1):
                dp[j] = min(dp[j], dp[left] + 1) # dp[left] is minTaps till before left
        
        if dp[-1] == math.inf:
            return -1
        return dp[-1]
