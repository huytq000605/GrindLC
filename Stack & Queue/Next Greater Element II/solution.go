package main

func nextGreaterElements(nums []int) []int {
	stack := []int{}
	result := make([]int, len(nums))
	for i := 0; i < len(result); i++ {
		result[i] = -1
	}
	for i := 0; i < 2*len(nums); i++ {
		for len(stack) > 0 && nums[stack[len(stack)-1]] < nums[i%len(nums)] {
			result[stack[len(stack)-1]] = nums[i%len(nums)]
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, i%len(nums))
	}
	return result
}
