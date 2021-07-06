package main

import "sort"

func subsetsWithDup(nums []int) [][]int {
	result := make([][]int, 0)
	result = append(result, []int{})
	current := make([]int, 0)
	sort.Ints(nums)
	helper(nums, 0, &current, &result)
	return result
}

func helper(nums []int, index int, current *[]int, result *[][]int) {
	if index == len(nums) {
		return
	}
	*current = append(*current, nums[index])
	toBePushed := make([]int, 0)
	toBePushed = append(toBePushed, (*current)...)
	*result = append(*result, toBePushed)
	helper(nums, index+1, current, result)
	*current = (*current)[0 : len(*current)-1]
	added := nums[index]
	for index < len(nums) && nums[index] == added {
		index++
	}
	helper(nums, index, current, result)
}
