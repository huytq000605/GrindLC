package main

/*
A+B+C+D = 0 <=> A+B = -C-D
*/

func fourSumCount(nums1 []int, nums2 []int, nums3 []int, nums4 []int) int {
	n := len(nums1)
	result := 0
	sumMap := make(map[int]int)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			sumMap[nums1[i]+nums2[j]]++
		}
	}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			sum := nums3[i] + nums4[j]
			if mutiplier, ok := sumMap[-sum]; ok {
				result += mutiplier
			}
		}
	}
	return result
}
