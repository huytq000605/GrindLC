package main

import "sort"

func subsetsWithDup(nums []int) [][]int {
	result := make([][]int, 0)
	sort.Ints(nums)
	recursiv(nums, 0, []int{}, &result)
	return result
}

func recursiv(nums []int, idx int, current []int, result *[][]int) {
	copyCurrent := make([]int, 0) // We dont want to insert the reference of current to result because we will mutate it through out the loop
	copyCurrent = append(copyCurrent, current...)
	*result = append(*result, copyCurrent)
	for i := idx; i < len(nums); i++ {
		if i > idx && nums[i] == nums[i-1] {
			continue
		}
		current = append(current, nums[i])
		recursiv(nums, i+1, current, result)
		current = current[:len(current)-1]

	}
}
