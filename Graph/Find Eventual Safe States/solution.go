package main

import "sort"

func eventualSafeNodes(graph [][]int) []int {
	cache := make(map[int]bool)
	result := make([]int, 0)
	for index := range graph {
		seen := make(map[int]bool)
		dfs(graph, index, seen, cache, &result)
	}
	sort.Ints(result)
	return result
}

func dfs(graph [][]int, index int, seen map[int]bool, cache map[int]bool, result *[]int) bool {
	if _, ok := cache[index]; ok {
		return cache[index]
	}
	if seen[index] {
		return true
	}
	seen[index] = true
	for _, node := range graph[index] {
		isCicular := dfs(graph, node, seen, cache, result)
		if isCicular == true {
			cache[index] = true
			return true
		}
	}
	*result = append(*result, index)
	cache[index] = false
	return false
}
