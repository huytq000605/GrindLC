package main

/*
Kadane's algorithm.
*/

import "math"

func maxSubArray(nums []int) int {
	max := math.MinInt32
	curr := math.MinInt32
	for _, num := range nums {
		if curr+num <= num {
			curr = num
		} else {
			curr += num
		}
		if curr > max {
			max = curr
		}
	}
	return max
}
