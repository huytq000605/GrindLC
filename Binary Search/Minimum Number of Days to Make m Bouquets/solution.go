package main

import "math"

func minDays(bloomDay []int, m int, k int) int {
	if k*m > len(bloomDay) {
		return -1
	}

	min := math.MaxInt32
	max := math.MinInt32

	for _, day := range bloomDay {
		if min > day {
			min = day
		}
		if max < day {
			max = day
		}
	}
	max = max + 1

	for min < max {
		middle := min + (max-min)/2
		count := 0
		bouquets := 0
		for _, day := range bloomDay {
			if day <= middle {
				count++
				if count == k {
					bouquets++
					count = 0
				}
			} else {
				count = 0
			}
		}
		if bouquets < m {
			min = middle + 1
		} else {
			max = middle
		}
	}
	return min
}
