package main

func criticalConnections(n int, connections [][]int) [][]int {
	graph := make([][]int, n)
	for i := 0; i < n; i++ {
		graph[i] = make([]int, 0)
	}
	for _, edge := range connections {
		u, v := edge[0], edge[1]
		graph[u] = append(graph[u], v)
		graph[v] = append(graph[v], u)
	}

	idxs := make([]int, n)
	for i := 0; i < n; i++ {
		idxs[i] = -1
	}
	idx := 0
	lowest := make([]int, n)
	for i := 0; i < n; i++ {
		lowest[i] = -1
	}
	result := make([][]int, 0)

	var dfs func(int, int) int
	dfs = func(u int, parent int) int {
		if lowest[u] != -1 {
			return lowest[u]
		}
		lowest[u] = idx
		idxs[u] = idx
		initial := idx
		idx += 1

		for _, v := range graph[u] {
			if v == parent {
				continue
			}
			if lowest[v] == -1 {
				dfs(v, u)
			}
			if lowest[v] < lowest[u] {
				lowest[u] = lowest[v]
			}
			if lowest[v] > initial {
				result = append(result, []int{u, v})
			}
		}
		return lowest[u]
	}
	dfs(0, -1)
	return result
}
