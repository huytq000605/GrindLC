package main

import "strings"

func camelMatch(queries []string, pattern string) []bool {
	result := make([]bool, len(queries))
	patternArr := strings.Split(pattern, "")
	for idx, query := range queries {
		res := checkPattern(strings.Split(query, ""), patternArr)
		result[idx] = res
	}
	return result
}

/*
We use 2 pointer to check for match
*/
func checkPattern(query []string, pattern []string) bool {
	patternIdx := 0
	for queryIdx := range query {
		if patternIdx < len(pattern) && query[queryIdx] == pattern[patternIdx] {
			patternIdx++
		} else {
			if strings.ToUpper(query[queryIdx]) == query[queryIdx] {
				return false
			}
		}
	}
	if patternIdx == len(pattern) {
		return true
	}
	return false
}
