package main

func minOperations(nums1 []int, nums2 []int) int {
	if 1*len(nums1) > 6*len(nums2) || 6*len(nums1) < 1*len(nums2) {
		return -1
	}
	sum1 := 0
	sum2 := 0
	for _, num := range nums1 {
		sum1 += num
	}
	for _, num := range nums2 {
		sum2 += num
	}
	var difference int
	if sum1 > sum2 {
		nums1, nums2 = nums2, nums1
		difference = sum1 - sum2
	} else {
		difference = sum2 - sum1
	}
	changes := make(map[int]int)
	for _, num := range nums1 {
		changes[6-num]++
	}
	for _, num := range nums2 {
		changes[num-1]++
	}
	change := 5
	operations := 0
	for difference > 0 {
		for changes[change] > 0 && difference > 0 {
			operations++
			difference -= change
			changes[change]--
		}
		change--
	}
	return operations
}
