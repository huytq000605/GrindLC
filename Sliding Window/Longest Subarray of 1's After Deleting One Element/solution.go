package main

func longestSubarray(nums []int) int {
	max := 0
	start := 0
	idxZero := -1
	for i := 0; i < len(nums); i++ {
		if nums[i] == 0 {
			start = idxZero + 1
			idxZero = i
		}
		if i-start+1 > max {
			max = i - start + 1
		}
	}

	return max - 1
}
