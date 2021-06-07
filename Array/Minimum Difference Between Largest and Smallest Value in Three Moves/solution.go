package main

import "sort"

func minDifference(nums []int) int {
	if len(nums) <= 4 {
		return 0
	}
	sort.Ints(nums)
	result := 99999999999
	end := len(nums) - 1
	for i := 0; i <= 3; i++ {
		diff := nums[end-(3-i)] - nums[i]
		if diff < result {
			result = diff
		}
	}
	return result
}
