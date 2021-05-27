package main

/*
Heap Solution: result for saving all min values from 1th to kth
idxArr to save index of each row, first all will be 0

*/

func kthSmallest(matrix [][]int, k int) int {
	n := len(matrix)
	result := make([]int, k)
	idxArr := make([]int, n)
	idx := 0
	for i := 0; i < k; i++ { // We need kth min so we loop k times
		min := 99999999999
		for j := 0; j < n; j++ { // Loop through all current min of each row, the smallest is the next min of result
			if idxArr[j] == n {
				continue
			}
			if matrix[j][idxArr[j]] <= min {
				min = matrix[j][idxArr[j]]
				idx = j
			}
		}
		idxArr[idx]++
		result[i] = min
	}
	return result[k-1]
}
