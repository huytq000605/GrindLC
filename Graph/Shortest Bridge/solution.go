func shortestBridge(grid [][]int) int {
	seen := make(map[string]bool)
	queue := make([][]int, 0)
findFirstIsland:
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == 1 {
				dfs(grid, i, j, seen, &queue)
				break findFirstIsland
			}
		}
	}
	directions := [][]int{{0, 1}, {1, 0}, {-1, 0}, {0, -1}}
	for len(queue) > 0 {
		row := queue[0][0]
		col := queue[0][1]
		distance := queue[0][2]
		queue = queue[1:]
		if row < 0 || row >= len(grid) || col < 0 || col >= len(grid[0]) {
			continue
		}
		key := fmt.Sprintf("%v-%v", row, col)
		if seen[key] == true && distance != 0 {
			continue
		}
		if seen[key] == false && grid[row][col] == 1 {
			return distance - 1
		}
		seen[key] = true
		for _, direction := range directions {
			queue = append(queue, []int{row + direction[0], col + direction[1], distance + 1})
		}

	}
	return 0
}

func dfs(grid [][]int, row int, col int, island map[string]bool, queue *[][]int) {
	if row < 0 || row >= len(grid) || col < 0 || col >= len(grid[0]) || grid[row][col] == 0 {
		return
	}
	key := fmt.Sprintf("%v-%v", row, col)
	if _, ok := island[key]; ok {
		return
	}
	island[key] = true
	directions := [][]int{{0, 1}, {1, 0}, {-1, 0}, {0, -1}}
	for _, direction := range directions {
		dfs(grid, row+direction[0], col+direction[1], island, queue)
	}
	*queue = append(*queue, []int{row, col, 0})
}