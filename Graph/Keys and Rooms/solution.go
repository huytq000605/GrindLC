package main

func canVisitAllRooms(rooms [][]int) bool {
	numOfRooms := 1
	seen := make(map[int]bool)
	seen[0] = true
	for _, key := range rooms[0] {
		numOfRooms += dfs(rooms, key, seen)
	}
	return numOfRooms == len(rooms)
}

func dfs(rooms [][]int, curr int, seen map[int]bool) int {
	if _, ok := seen[curr]; ok {
		return 0
	}
	seen[curr] = true
	result := 1
	for _, key := range rooms[curr] {
		result += dfs(rooms, key, seen)
	}
	return result
}
