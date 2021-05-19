package main

import "math"

func maxDistance(nums1 []int, nums2 []int) int {
	result := 0
	for i := 0; i < len(nums1); i++ {
		min := i
		max := len(nums2) - 1
		for min < max {
			middle := int(math.Ceil(float64(max+min) / float64(2)))
			if nums1[i] > nums2[middle] {
				max = middle - 1
			} else {
				min = middle
			}
		}
		if nums1[i] <= nums2[max] {
			if result < (max - i) {
				result = max - i
			}
		}
	}
	return result
}
