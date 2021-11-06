package main

import "math"

func minScoreTriangulation(values []int) int {
	dp := make([][]int, len(values))
	for i := range dp {
		dp[i] = make([]int, len(values))
	}

	var dfs func(start int, end int) int
	dfs = func(start int, end int) int {
		if start+1 == end {
			return 0
		}
		if dp[start][end] != 0 {
			return dp[start][end]
		}
		result := math.MaxInt32
		for i := start + 1; i < end; i++ {
			res := values[start]*values[i]*values[end] + dfs(start, i) + dfs(i, end)
			if res < result {
				result = res
			}
		}
		dp[start][end] = result
		return result
	}
	return dfs(0, len(values)-1)
}
