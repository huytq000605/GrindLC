class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [poured]
        for row in range(1, query_row+1):
            next_dp = [0 for _ in range(row + 1)]
            for col in range(row):
                if dp[col] < 1: continue
                next_dp[col] += (dp[col] - 1)/2
                next_dp[col+1] += (dp[col] - 1)/2
                
            dp = next_dp
        return min(1.0, dp[query_glass])
