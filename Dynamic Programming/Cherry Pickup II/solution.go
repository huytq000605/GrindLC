package main

func cherryPickup(grid [][]int) int {
	cache := make([][][]int, len(grid))
	for i := range cache {
		cache[i] = make([][]int, len(grid[0]))
		for j := range cache[i] {
			cache[i][j] = make([]int, len(grid[0]))
			for k := range cache[i][j] {
				cache[i][j][k] = -1
			}
		}
	}
	return dfs(grid, 0, 0, len(grid[0])-1, cache)
}

func dfs(grid [][]int, row int, col1 int, col2 int, cache [][][]int) int {
	if row >= len(grid) || col1 < 0 || col1 >= len(grid[0]) || col2 < 0 || col2 >= len(grid[0]) {
		return 0
	}
	if cache[row][col1][col2] > -1 {
		return cache[row][col1][col2]
	}
	thisRow := 0
	if col1 == col2 {
		thisRow = grid[row][col1]
	} else {
		thisRow = grid[row][col1] + grid[row][col2]
	}
	belowThisRow := 0
	for i := -1; i <= 1; i++ {
		for j := -1; j <= 1; j++ {
			res := dfs(grid, row+1, col1+i, col2+j, cache)
			if res > belowThisRow {
				belowThisRow = res
			}
		}
	}
	cache[row][col1][col2] = belowThisRow + thisRow
	return cache[row][col1][col2]

}
