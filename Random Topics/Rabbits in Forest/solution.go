package main

func numRabbits(answers []int) int {
	seen := make(map[int]int)
	result := 0
	for _, answer := range answers {
		seen[answer] = seen[answer] + 1
	}
	for key, value := range seen {
		rabbitsInEachGroup := key + 1                              // number of rabbits in each group
		current := value / rabbitsInEachGroup * rabbitsInEachGroup // number of groups * numbers of rabbits in each group
		if value-current > 0 {                                     // the rest of rabbits cant make a full group still make a group with some rabbits are not answering question
			result += rabbitsInEachGroup
		}
		result += current

	}
	return result
}
