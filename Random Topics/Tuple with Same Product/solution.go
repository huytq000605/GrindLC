package main

import (
	"sort"
)

/*
Save freq of all mutiply result for each element with every element behind it in a map
for each freq > 1 then we can create a tuple, we can have freq selection for first 2, have freq - 1 selection for rest 2, then 2! for each 2
*/

func tupleSameProduct(nums []int) int {
	sort.Ints(nums)
	result := 0
	tupleMap := make(map[int]int)
	for i := range nums {
		for j := i + 1; j < len(nums); j++ {
			if _, ok := tupleMap[nums[i]*nums[j]]; ok {
				tupleMap[nums[i]*nums[j]] = tupleMap[nums[i]*nums[j]] + 1
			} else {
				tupleMap[nums[i]*nums[j]] = 1
			}

		}
	}
	for _, value := range tupleMap {
		if value > 1 {
			result += value * (value - 1) * 2 * 2
		}
	}
	return result
}
