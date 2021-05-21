package main

func longestSubarray(nums []int) int {
	max := 0
	start := 0
	idxZero := make([]int, 0)
	for i := 0; i < len(nums); i++ {
		if nums[i] == 0 {
			idxZero = append(idxZero, i)
			if len(idxZero) > 1 {
				start = idxZero[0] + 1
				idxZero = idxZero[1:]
			}
		}
		if i-start+1 > max {
			max = i - start + 1
		}
	}

	return max - 1
}
