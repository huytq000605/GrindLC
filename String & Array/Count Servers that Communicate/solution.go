package main

/*
We count number of servers on every row and col and save it to array
the second iterate we check if any servers is isolated then we leave it out
*/

func countServers(grid [][]int) int {
	rowCount := make([]int, len(grid))
	colCount := make([]int, len(grid[0]))
	totalServers := 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == 1 {
				rowCount[i]++
				colCount[j]++
				totalServers++
			}
		}
	}
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == 1 && rowCount[i] == 1 && colCount[j] == 1 {
				totalServers--
			}
		}
	}
	return totalServers
}
