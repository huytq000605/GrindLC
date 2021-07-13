package main

import "math"

func kthSmallest(matrix [][]int, k int) int {
	min := matrix[0][0]
	n := len(matrix)
	max := matrix[n-1][n-1]

	for min < max {
		mid := int(math.Floor(float64(min+max) / 2))
		count := 0
		for i := n - 1; i >= 0; i-- {
			for j := n - 1; j >= 0; j++ {
				if matrix[i][j] <= mid {
					count += j + 1
					break
				}
			}
		}
		if count < k {
			min = mid + 1
		} else {
			max = mid
		}
	}
	return min
}
