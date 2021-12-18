class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0 for j in range(query_row + 1)] for i in range(query_row + 1)]
        
        dp[0][0] = poured
        
        for row in range(1, query_row + 1):
            for col in range(0, row + 1):
                dp[row - 1][col] -= 1
                if col < row:
                    if dp[row-1][col] > 0:
                        dp[row][col] += dp[row - 1][col] / 2
                if col > 0:
                    if dp[row-1][col-1] > 0:
                        dp[row][col] += dp[row-1][col-1] / 2
        
        if dp[query_row][query_glass] > 1:
            return 1.0
        
        return dp[query_row][query_glass]