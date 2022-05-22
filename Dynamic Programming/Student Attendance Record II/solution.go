package main

import "math"

func checkRecord(n int) int {
	seen := make([][][]int, n)
	for i := 0; i < n; i++ {
		seen[i] = make([][]int, 2)
		for j := 0; j < 2; j++ {
			seen[i][j] = make([]int, 3)
			for k := 0; k < 3; k++ {
				seen[i][j][k] = -1
			}
		}
	}
	MOD := int(math.Pow(10, 9)) + 7
	var dfs func(i, j, k int) int
	dfs = func(i, j, k int) int {
		if j >= 2 {
			return 0
		}
		if k >= 3 {
			return 0
		}
		if i >= n {
			return 1
		}
		if seen[i][j][k] != -1 {
			return seen[i][j][k]
		}
		result := dfs(i+1, j, 0) + dfs(i+1, j+1, 0) + dfs(i+1, j, k+1)
		result %= MOD
		seen[i][j][k] = result
		return result
	}
	return dfs(0, 0, 0)
}
