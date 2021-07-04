package main

func numIslands(grid [][]byte) int {
	islands := 0
	cache := make([][]int, len(grid))
	for i := range cache {
		cache[i] = make([]int, len(grid[0]))
	}
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == '1' && cache[i][j] == 0 {
				dfs(grid, i, j, cache)
				islands++
			}
		}
	}
	return islands
}

func dfs(grid [][]byte, row int, col int, cache [][]int) {
	if row < 0 || row >= len(grid) || col < 0 || col >= len(grid[0]) || grid[row][col] == '0' || cache[row][col] == 1 {
		return
	}
	cache[row][col] = 1
	directions := [][]int{{0, 1}, {1, 0}, {-1, 0}, {0, -1}}
	for _, direction := range directions {
		dfs(grid, row+direction[0], col+direction[1], cache)
	}

}
