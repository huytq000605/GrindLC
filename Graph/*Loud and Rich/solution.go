package main

func loudAndRich(richer [][]int, quiet []int) []int {
	richerMap := make(map[int][]int)
	for _, rich := range richer {
		richerMap[rich[1]] = append(richerMap[rich[1]], rich[0])
	}

	result := make([]int, len(quiet))
	seen := make(map[int]int)

	for i := 0; i < len(result); i++ {
		result[i] = dfs(i, seen, richerMap, quiet)
	}
	return result

}

func dfs(currentPerson int, seen map[int]int, richerMap map[int][]int, quiet []int) int {
	if _, ok := seen[currentPerson]; ok {
		return seen[currentPerson]
	}

	result := currentPerson
	for _, richerPerson := range richerMap[currentPerson] {
		res := dfs(richerPerson, seen, richerMap, quiet)
		if quiet[res] < quiet[result] {
			result = res
		}
	}
	seen[currentPerson] = result
	return result
}
