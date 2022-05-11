package main

func countVowelStrings(n int) int {
	dp := make([][6]int, n+1)
	for i := 1; i < 6; i++ {
		dp[1][i] = 1
	}
	for i := 2; i <= n; i++ {
		for j := 1; j < 6; j++ {
			for k := 1; k <= j; k++ {
				dp[i][k] += dp[i-1][j]
			}
		}
	}
	result := 0
	for i := 1; i < 6; i++ {
		result += dp[n][i]
	}
	return result
}
