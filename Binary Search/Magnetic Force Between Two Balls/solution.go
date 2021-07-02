package main

import "sort"

func maxDistance(position []int, m int) int {
	sort.Ints(position)
	min := 1
	max := position[len(position)-1] - position[0]
	for min < max {
		mid := min + (max-min+1)/2

		count := 0
		prevIdx := -1
		for i := range position {
			if i == 0 {
				count = 1
				prevIdx = 0
			} else if position[i]-position[prevIdx] >= mid {
				count++
				prevIdx = i
			}
		}

		if count < m {
			max = mid - 1
		} else {
			min = mid
		}
	}
	return min
}
