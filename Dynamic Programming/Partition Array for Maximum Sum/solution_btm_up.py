class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0 for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            mx = 0
            for j in range(i, i-k, -1):
                mx = max(mx, arr[j])
                dp[j] = max(dp[j], mx * (i - j + 1) + dp[i+1])
        return dp[0]

# Further Optimization
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0 for _ in range(k+1)]
        for i in range(n-1, -1, -1):
            dp = [0, *dp[:-1]]
            mx = 0
            for j in range(k):
                if i - j < 0: break
                mx = max(mx, arr[i-j])
                dp[k-1-j] = max(dp[k-1-j], mx * (j+1) + dp[k])     
        return max(dp)
