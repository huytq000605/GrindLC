package main

import (
	"math"
	"sort"
)

func minMoves2(nums []int) int {
	sort.Ints(nums)
	target := nums[len(nums)/2]
	result := 0
	for i := 0; i < len(nums); i++ {
		result += int(math.Abs(float64(nums[i] - target)))
	}
	return result
}
