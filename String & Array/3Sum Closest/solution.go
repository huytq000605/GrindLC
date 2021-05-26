package main

import (
	"math"
	"sort"
)

func threeSumClosest(nums []int, target int) int {
	min := 999999
	result := 0
	sort.Ints(nums)
	for i := 0; i < len(nums)-2; i++ {
		firstNum := nums[i]
		newTarget := target - firstNum
		secondIndex := i + 1
		thirdIndex := len(nums) - 1
		for secondIndex < thirdIndex {
			total := nums[secondIndex] + nums[thirdIndex]
			distance := int(math.Abs(float64(newTarget - total)))
			if distance < min {
				result = total + firstNum
				min = distance
				if min == 0 {
					return total + firstNum
				}
			}
			if total < newTarget {
				secondIndex++
			} else {
				thirdIndex--
			}
		}
	}
	return result
}
