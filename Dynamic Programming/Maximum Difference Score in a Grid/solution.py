class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = [-math.inf for _ in range(n)]
        result = -math.inf
        for i in range(n):
            if i - k >= 0:
                dp[i] = max(dp[i-k] + energy[i], energy[i])
            else:
                dp[i] = energy[i]
            if i + k >= n:
                result = max(result, dp[i])
        return result
            
