package main

import (
	"fmt"
	"math"
)

func minScoreTriangulation(values []int) int {
	cache := make(map[string]int)
	return helper(values, 0, len(values)-1, cache)
}

func helper(values []int, start int, end int, cache map[string]int) int {
	if end-start+1 < 3 {
		return 0
	}
	key := fmt.Sprintf("%v-%v", start, end)
	if result, ok := cache[key]; ok {
		return result
	}
	result := math.MaxInt32
	for i := start + 1; i < end; i++ {
		res := values[i]*values[start]*values[end] + helper(values, start, i, cache) + helper(values, i, end, cache)
		if res < result {
			result = res
		}
	}
	cache[key] = result
	return result
}
