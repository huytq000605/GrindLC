package main

/*
If the start -> end have k odd number, then there are [first indexOdd - start] sub contiguous array to result
*/

func longestOnes(nums []int, k int) int {
	start := 0
	result := 0
	idxZero := make([]int, 0)
	for end := range nums {
		if nums[end] == 0 {
			idxZero = append(idxZero, end)
			if len(idxZero) > k {
				start = idxZero[0] + 1
				idxZero = idxZero[1:]
			}
		}
		if end-start+1 > result {
			result = end - start + 1
		}
	}
	return result
}
