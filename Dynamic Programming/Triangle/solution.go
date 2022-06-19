package main

import "math"

func minimumTotal(triangle [][]int) int {
	prev := triangle[0]
	m := len(triangle)
	min := triangle[0][0]
	for row := 1; row < m; row++ {
		cur := make([]int, len(triangle[row]))
		min = math.MaxInt32
		for col := 0; col < len(triangle[row]); col++ {
			cur[col] = math.MaxInt32
			if col < len(prev) {
				cur[col] = prev[col] + triangle[row][col]
			}
			if col-1 >= 0 && prev[col-1]+triangle[row][col] < cur[col] {
				cur[col] = prev[col-1] + triangle[row][col]
			}
			if cur[col] < min {
				min = cur[col]
			}
		}
		prev = cur
	}
	return min
}
