package main

func maxChunksToSorted(arr []int) int {
	n := len(arr)
	left_max := make([]int, n)
	right_min := make([]int, n)
	left_max[0] = arr[0]
	right_min[n-1] = arr[n-1]
	result := 1

	for i := 1; i < n; i++ {
		if left_max[i-1] >= arr[i] {
			left_max[i] = left_max[i-1]
		} else {
			left_max[i] = arr[i]
		}
	}

	for i := n - 2; i >= 0; i-- {
		if right_min[i+1] <= arr[i] {
			right_min[i] = right_min[i+1]
		} else {
			right_min[i] = arr[i]
		}
	}

	for i := 0; i < n-1; i++ {
		if left_max[i] <= right_min[i+1] {
			result += 1
		}
	}
	return result
}
