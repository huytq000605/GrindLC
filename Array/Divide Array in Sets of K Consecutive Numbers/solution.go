package main

import "sort"

type pos []int

func isPossibleDivide(nums []int, k int) bool {
	freq := make(map[int]pos)
	sort.Ints(nums)
	indexUsed := make(map[int]bool)
	for i := 0; i < len(nums); i++ {
		if _, ok := freq[nums[i]]; !ok {
			freq[nums[i]] = make(pos, 0)
		}
		freq[nums[i]] = append(freq[nums[i]], i)
	} // Freq map with index in each key
	for i := 0; i < len(nums); i++ {
		if _, ok := indexUsed[i]; ok {
			continue
		}
		currentValue := nums[i]
		for j := 0; j < k; j++ { // Find all the next value
			if len(freq[currentValue]) > 0 {
				indexUsed[freq[currentValue][0]] = true
				freq[currentValue] = freq[currentValue][1:]
				currentValue = currentValue + 1
			} else {
				return false
			}
		}
	}
	return true
}
