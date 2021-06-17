package main

import "fmt"

func maxAreaOfIsland(grid [][]int) int {
	seen := make(map[string]int)
	max := 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == 1 {
				current := dfs(grid, i, j, seen)
				if current > max {
					max = current
				}
			}

		}
	}
	return max
}

func dfs(grid [][]int, i int, j int, seen map[string]int) int {
	if i < 0 || i == len(grid) || j < 0 || j == len(grid[0]) || grid[i][j] == 0 {
		return 0
	}
	key := fmt.Sprintf("%v-%v", i, j)
	if _, ok := seen[key]; ok {
		return 0
	}
	seen[key] = 1
	result := 1 + dfs(grid, i+1, j, seen) + dfs(grid, i-1, j, seen) + dfs(grid, i, j-1, seen) + dfs(grid, i, j+1, seen)
	return result
}
