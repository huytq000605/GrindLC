package main

func canChoose(groups [][]int, nums []int) bool {
	currentGroup := 0
	matched := 0
	start := 0
	for start < len(nums) {
		if nums[start] == groups[currentGroup][0] {
			flag := true
			for i := 1; i < len(groups[currentGroup]); i++ {
				if start+i == len(nums) {
					flag = false
					break
				}
				if nums[start+i] != groups[currentGroup][i] {
					flag = false
					break
				}
			}
			if flag == true {
				matched++
				if matched == len(groups) {
					return true
				}
				start += len(groups[currentGroup]) - 1
				currentGroup++
			}
		}
		start++
	}
	return false
}
