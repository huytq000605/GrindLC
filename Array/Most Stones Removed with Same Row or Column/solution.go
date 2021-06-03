package main

import "fmt"

/*
Island is all element have the same row or column with atleast another element in the island
Each island is remove to have only 1 element
Then number of removed stones is numberOfStones - numberOfIslands
*/

func removeStones(stones [][]int) int {
	seen := make(map[string]int)
	numberOfStones := len(stones)
	numberOfIslands := 0
	for _, stone := range stones {
		numberOfIslands += helper(stones, stone, seen)
	}
	return numberOfStones - numberOfIslands
}

func helper(stones [][]int, current []int, seen map[string]int) int {
	key := fmt.Sprintf("%v-%v", current[0], current[1])
	if _, ok := seen[key]; ok {
		return 0
	}
	seen[key] = 1
	for _, stone := range stones {
		if stone[0] == current[0] || stone[1] == current[1] {
			helper(stones, stone, seen)
		}
	}
	return 1
}
