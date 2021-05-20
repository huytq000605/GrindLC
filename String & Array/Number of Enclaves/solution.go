package main

func numEnclaves(grid [][]int) int {
	result := 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if i == 0 || i == len(grid)-1 || j == 0 || j == len(grid[0])-1 {
				helper(&grid, i, j)
			}
		}
	}
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == 1 {
				result++
			}
		}
	}
	return result
}

func helper(grid *[][]int, i int, j int) {
	if i < 0 || j < 0 || i == len(*grid) || j == len((*grid)[0]) || (*grid)[i][j] == 0 {
		return
	}
	(*grid)[i][j] = 0
	helper(grid, i+1, j)
	helper(grid, i, j+1)
	helper(grid, i, j-1)
	helper(grid, i-1, j)

}
