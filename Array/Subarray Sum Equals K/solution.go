package main

func subarraySum(nums []int, k int) int {
	prefix := make([]int, len(nums))
	for i := range prefix {
		if i == 0 {
			prefix[i] = nums[i]
		} else {
			prefix[i] = prefix[i-1] + nums[i]
		}
	}
	result := 0
	seenSum := make(map[int]int)
	for _, sum := range prefix {
		if sum == k {
			result++
		}
		if _, ok := seenSum[sum-k]; ok {
			result += seenSum[sum-k]
		}
		seenSum[sum]++
	}
	return result
}
