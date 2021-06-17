package main

func makeConnected(n int, connections [][]int) int {
	if len(connections) < n-1 {
		return -1
	}
	graph := make([][]int, n)
	for i := 0; i < len(graph); i++ {
		graph[i] = make([]int, 0)
	}
	for _, connection := range connections {
		net1 := connection[0]
		net2 := connection[1]
		graph[net1] = append(graph[net1], net2)
		graph[net2] = append(graph[net2], net1)
	}
	connectedGroup := 0
	seen := make(map[int]bool)
	for i := 0; i < len(graph); i++ {
		connectedGroup += dfs(i, graph, seen)
	}
	return connectedGroup - 1
}

func dfs(from int, graph [][]int, seen map[int]bool) int {
	if _, ok := seen[from]; ok {
		return 0
	}
	seen[from] = true
	for _, to := range graph[from] {
		dfs(to, graph, seen)
	}

	return 1
}
