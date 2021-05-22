package main

import "sort"

func subsetsWithDup(nums []int) [][]int {
	result := make([][]int, 0)
	result = append(result, []int{})
	sort.Ints(nums)
	for i := range nums {
		if i >= 1 && nums[i] == nums[i-1] {
			continue
		}
		recursiv(nums, i, []int{}, &result)
	}
	return result
}

func recursiv(nums []int, idx int, current []int, result *[][]int) {
	current = append(current, nums[idx])
	*result = append(*result, current)
	for i := idx + 1; i < len(nums); i++ {
		if i != idx+1 && nums[i] == nums[i-1] {
			continue
		}
		oriCurrent := make([]int, 0)
		oriCurrent = append(oriCurrent, current...)
		recursiv(nums, i, current, result)
		current = oriCurrent
	}
}
