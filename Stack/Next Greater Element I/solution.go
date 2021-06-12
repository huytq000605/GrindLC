package main

func nextGreaterElement(nums1 []int, nums2 []int) []int {
	result := make([]int, len(nums1))
	for i := 0; i < len(result); i++ {
		result[i] = -1
	}
	nums1Map := map[int]int{}
	for i := 0; i < len(nums1); i++ {
		nums1Map[nums1[i]] = i
	}
	stack := []int{}
	for i := 0; i < len(nums2); i++ {
		for len(stack) > 0 && nums2[i] > stack[len(stack)-1] {
			index, ok := nums1Map[stack[len(stack)-1]]
			if ok {
				result[index] = nums2[i]
			}
			stack = stack[0 : len(stack)-1]
		}
		stack = append(stack, nums2[i])
	}
	return result
}
