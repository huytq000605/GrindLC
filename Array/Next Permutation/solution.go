package main

// According to Wikipedia, a man named Narayana Pandita presented the following simple algorithm to solve this problem in the 14th century.

// Find the largest index k such that nums[k] < nums[k + 1]. If no such index exists, just reverse nums and done.
// Find the largest index l > k such that nums[k] < nums[l].
// Swap nums[k] and nums[l].
// Reverse the sub-array nums[k + 1:].

func nextPermutation(nums []int) {
	for i := len(nums) - 2; i >= 0; i-- {
		if nums[i] < nums[i+1] {
			index := i
			min := index + 1
			max := len(nums) - 1
			for min < max {
				mid := min + (max-min+1)/2
				if nums[mid] > nums[index] {
					min = mid
				} else {
					max = mid - 1
				}
			}
			nums[index], nums[min] = nums[min], nums[index]
			reverse(nums, index+1, len(nums)-1)
			return
		}
	}
	reverse(nums, 0, len(nums)-1)
	return
}

func reverse(nums []int, start int, end int) {
	arr := make([]int, end-start+1)
	idx := 0
	for i := end; i >= start; i-- {
		arr[idx] = nums[i]
		idx++
	}
	idx = 0
	for i := start; i <= end; i++ {
		nums[i] = arr[idx]
		idx++
	}
}
