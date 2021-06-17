func numberOfArithmeticSlices(nums []int) int {
	if len(nums) < 3 {
		return 0
	}
	result := 0
	dp := make([]int, len(nums))            // Number of Arithmetic Slice ended by nums[i]
	if nums[2]-nums[1] == nums[1]-nums[0] { // If the first 3 number are Arithmetic Slice
		dp[2] = 1
	}
	result = dp[2]
	for i := 3; i < len(nums); i++ {
		if nums[i]-nums[i-1] == nums[i-1]-nums[i-2] {
			/*
				*	So basically, number Arithmetic Slice ended by nums[i+1] = number number of Arithmetic Slice ended by nums[i] + 1
					*	because all Arithmetic Slice ended by nums[i] append nums[i+1] is still Arithmetic Slice,
					* the only new one we construct is the nums[i-1], nums[i], nums[i+1]
			*/
			dp[i] = dp[i-1] + 1
			result += dp[i]
		}
	}

	return result
}
