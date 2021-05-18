/*
Use recursion helper function, helper will start at idx and get every element after idx append to current, append current to result
*/

package main

func subsets(nums []int) [][]int {
	result := make([][]int, 0)
	for i := 0; i < len(nums); i++ {
		current := make([]int, 0)
		helper(&nums, i, &current, &result)
	}
	result = append(result, []int{})
	return result
}

func helper(nums *[]int, idx int, current *[]int, result *[][]int) {
	if idx == len(*nums) {
		return
	}
	*current = append(*current, (*nums)[idx])
	*result = append(*result, *current)
	for i := idx + 1; i < len(*nums); i++ {
		original := make([]int, len(*current))
		copy(original, *current)
		helper(nums, i, current, result)
		*current = original
	}
}
