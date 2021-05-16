package main

import (
	"fmt"
	"math"
)

// MAIN FUNCTION
func minimumDeleteSum(s1 string, s2 string) int {
	hashMap := make(map[string]int)
	result := helper(s1, s2, 0, 0, &hashMap)
	return result
}

// Sum of all ASCII number of s[i:]
func deadEndSum(s string, idx int) int {
	result := 0
	for i := idx; i < len(s); i++ {
		result += int(s[i])
	}
	return result
}

// Math.min in JS for ints in go
func MinInt(nums ...int) int {
	result := math.MaxUint32
	for _, v := range nums {
		if v < result {
			result = v
		}
	}
	return result
}

// Recursive function, use shared Hash Map to memoization
func helper(s1 string, s2 string, start1 int, start2 int, hashMap *map[string]int) int {
	key := fmt.Sprintf("%v-%v", start1, start2)
	if _, ok := (*hashMap)[key]; ok {
		return (*hashMap)[key]
	}
	result := 0
	if start1 == len(s1) || start2 == len(s2) {
		if start1 == len(s1) && start2 == len(s2) {
			return 0
		}
		if start1 == len(s1) {
			(*hashMap)[key] = deadEndSum(s2, start2)
			return (*hashMap)[key]
		} else {
			(*hashMap)[key] = deadEndSum(s1, start1)
			return (*hashMap)[key]
		}
	}

	if s1[start1] == s2[start2] {
		result += helper(s1, s2, start1+1, start2+1, hashMap)
	} else {
		temp1 := helper(s1, s2, start1+1, start2, hashMap) + int(s1[start1])
		temp2 := helper(s1, s2, start1, start2+1, hashMap) + int(s2[start2])
		result += MinInt(temp1, temp2)

	}
	(*hashMap)[key] = result
	return (*hashMap)[key]
}
