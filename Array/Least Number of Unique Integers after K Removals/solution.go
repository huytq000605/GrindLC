package main

import "sort"

func findLeastNumOfUniqueInts(arr []int, k int) int {
	counter := make(map[int]int)
	for i := 0; i < len(arr); i++ {
		counter[arr[i]] = counter[arr[i]] + 1
	}
	uniqueIntegers := len(counter)
	freqs := make([]int, 0)
	for _, value := range counter {
		freqs = append(freqs, value)
	}
	sort.Ints(freqs)
	removed := 0
	for _, freq := range freqs {
		if freq > k {
			break
		} else {
			k -= freq
			removed++
		}
	}
	return uniqueIntegers - removed
}
