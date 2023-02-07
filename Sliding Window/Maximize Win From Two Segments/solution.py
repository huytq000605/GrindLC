class Solution:
    def maximizeWin(self, prizes: List[int], k: int) -> int:
        j = 0
        n = len(prizes)
        # follow up for m segments
        # dp = [[0 for j in range(m+1)] for i in range(n+1)]
        dp = [0 for _ in range(n+1)]
        result = 0
        for i in range(n):
            while prizes[i] - prizes[j] > k:
                j += 1
            # dp[i+1][1] = max(dp[i][1], i-j+1)
            # for segment in range(2, m+1):
            #   dp[i+1][m] = max(dp[i+1][m], dp[j][m-1] + i - j + 1)
            dp[i+1] = max(dp[i], i-j+1)
            result = max(result, i - j + 1 + dp[j])
        # return dp[n][m]
        return result
    
            
            
