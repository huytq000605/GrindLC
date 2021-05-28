package main

func minPathSum(grid [][]int) int {
	dp := make([][]int, len(grid)+1)
	for i := 0; i < len(dp); i++ {
		dp[i] = make([]int, len(grid[0])+1)
	}
	for i := 1; i < len(dp); i++ {
		for j := 1; j < len(dp[0]); j++ {
			if i == 1 {
				dp[i][j] = dp[i][j-1] + grid[i-1][j-1]
				continue
			}
			if j == 1 {
				dp[i][j] = dp[i-1][j] + grid[i-1][j-1]
				continue
			}
			dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
		}
	}
	return dp[len(grid)][len(grid[0])]
}

func min(x, y int) int {
	if x > y {
		return y
	} else {
		return x
	}
}
