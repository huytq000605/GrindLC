package main

func minPatches(nums []int, n int) int {
	idx := 0
	sum := 0
	m := len(nums)
	result := 0
	for sum < n {
		if idx < m && nums[idx] <= sum+1 {
			sum += nums[idx]
			idx += 1
		} else {
			result += 1
			sum += sum + 1
		}
	}
	return result
}
