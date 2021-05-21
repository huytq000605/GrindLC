func longestOnes(nums []int, k int) int {
	start := 0
	countZero := 0
	max := 0
	for end := 0; end < len(nums); end++ {
		if nums[end] == 0 {
			countZero++
		}
		for countZero > k {
			if nums[start] == 0 {
				countZero--
			}
			start++
		}
		if max < end-start+1 {
			max = end - start + 1
		}
	}
	return max

}