package main

import "sort"

type pair [2]int

func getKth(lo int, hi int, k int) int {
	power := make([]pair, hi-lo+1)
	memo := make(map[int]int)
	for i := 0; i < len(power); i++ {
		power[i] = pair{getPower(lo, memo), lo}
		lo++
	}
	sort.SliceStable(power, func(i, j int) bool {
		return power[i][0] < power[j][0]
	})

	return power[k-1][1]
}

func getPower(num int, memo map[int]int) int {
	if num == 1 {
		return 0
	}
	if res, ok := memo[num]; ok {
		return res
	}
	if num%2 == 0 {
		memo[num] = 1 + getPower(num/2, memo)
	} else {
		memo[num] = 1 + getPower(3*num+1, memo)
	}
	return memo[num]
}
