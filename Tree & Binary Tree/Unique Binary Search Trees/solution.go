package main

func numTrees(n int) int {
	memo := make(map[int]int)
	return countTrees(n, 1, n, memo)
}

func countTrees(n int, start int, end int, memo map[int]int) int {
	if start >= end {
		return 1
	}
	if _, ok := memo[end-start]; ok {
		return memo[end-start]
	}
	result := 0
	for i := start; i <= end; i++ {
		left := countTrees(n, start, i-1, memo)
		right := countTrees(n, i+1, end, memo)
		result += left * right
	}
	memo[end-start] = result
	return result
}
