package main

func maxOperations(nums []int, k int) int {
	result := 0
	hashMap := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		if value := hashMap[nums[i]]; value > 0 {
			result++
			hashMap[nums[i]]--
			continue
		}
		hashMap[k-nums[i]]++
	}
	return result
}
