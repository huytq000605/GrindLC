package main

import "fmt"

func uniquePathsIII(grid [][]int) int {
	var startX, startY, endX, endY, emptySquares int
	seen := make(map[string]bool)
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == 1 {
				startX = i
				startY = j
			}
			if grid[i][j] == 2 {
				endX = i
				endY = j
			}
			if grid[i][j] == 0 {
				emptySquares++
			}
		}
	}
	return helper(grid, startX, startY, endX, endY, emptySquares, seen)
}

func helper(grid [][]int, i int, j int, endX int, endY int, emptySquares int, seen map[string]bool) int {
	if i < 0 || i == len(grid) || j < 0 || j == len(grid[0]) || grid[i][j] == -1 {
		return 0
	}
	if i == endX && j == endY {
		if len(seen) == emptySquares+1 {
			return 1
		} else {
			return 0
		}
	}
	key := fmt.Sprintf("%v-%v", i, j)
	if _, ok := seen[key]; ok {
		return 0
	}
	seen[key] = true
	result := 0
	oriMap := make(map[string]bool)
	copyMap(seen, oriMap)
	result += helper(grid, i+1, j, endX, endY, emptySquares, seen)
	seen = map[string]bool{}
	copyMap(oriMap, seen)
	result += helper(grid, i-1, j, endX, endY, emptySquares, seen)
	seen = map[string]bool{}
	copyMap(oriMap, seen)
	result += helper(grid, i, j+1, endX, endY, emptySquares, seen)
	seen = map[string]bool{}
	copyMap(oriMap, seen)
	result += helper(grid, i, j-1, endX, endY, emptySquares, seen)
	seen = map[string]bool{}
	copyMap(oriMap, seen)
	return result
}

func copyMap(src, dest map[string]bool) {
	for key, value := range src {
		dest[key] = value
	}
}
