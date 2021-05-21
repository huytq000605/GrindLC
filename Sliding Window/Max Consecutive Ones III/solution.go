package main

/*
If the start -> end have k odd number, then there are [first indexOdd - start] sub contiguous array to result
*/

func numberOfSubarrays(nums []int, k int) int {
	result := 0
	idxOdd := make([]int, 0)
	start := 0

	for end := range nums {
		if nums[end]%2 == 1 {
			idxOdd = append(idxOdd, end)
			if len(idxOdd) > k {
				start = idxOdd[0] + 1
				idxOdd = idxOdd[1:]
			}
		}
		if len(idxOdd) == k {
			result += idxOdd[0] - start + 1
		}
	}
	return result
}
