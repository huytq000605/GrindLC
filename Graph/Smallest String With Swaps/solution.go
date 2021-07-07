package main

import "sort"

func smallestStringWithSwaps(s string, pairs [][]int) string {
	arr := make([]byte, len(s))
	graph := make(map[int][]int)
	for _, pair := range pairs {
		if graph[pair[0]] == nil {
			graph[pair[0]] = make([]int, 0)
		}
		if graph[pair[1]] == nil {
			graph[pair[1]] = make([]int, 0)
		}
		graph[pair[0]] = append(graph[pair[0]], pair[1])
		graph[pair[1]] = append(graph[pair[1]], pair[0])
	}

	seen := make(map[int]bool)
	for i := range s {
		if graph[i] == nil {
			arr[i] = s[i]
		}
		byteArr := make([]byte, 0)
		indexArr := make([]int, 0)
		if seen[i] == false {
			dfs(s, i, graph, seen, &byteArr, &indexArr)
		}
		sort.Slice(byteArr, func(i, j int) bool {
			return byteArr[i] < byteArr[j]
		})
		sort.Ints(indexArr)
		for i := range byteArr {
			arr[indexArr[i]] = byteArr[i]
		}

	}

	return string(arr)

}

func dfs(s string, index int, graph map[int][]int, seen map[int]bool, byteArr *[]byte, indexArr *[]int) {
	if seen[index] == true {
		return
	}
	seen[index] = true
	*byteArr = append(*byteArr, s[index])
	*indexArr = append(*indexArr, index)
	for _, connectIndex := range graph[index] {
		dfs(s, connectIndex, graph, seen, byteArr, indexArr)
	}
}
