package main

/*
Kadane's algorithm.
*/

func maxSubArray(nums []int) int {
	dp := make([]int, len(nums))
	dp[0] = nums[0]
	for i := 1; i < len(nums); i++ {
		res := dp[i-1] + nums[i]
		if res > nums[i] {
			dp[i] = res
		} else {
			dp[i] = nums[i]
		}
	}
	result := dp[0]
	for i := 1; i < len(dp); i++ {
		if dp[i] > result {
			result = dp[i]
		}
	}
	return result
}
