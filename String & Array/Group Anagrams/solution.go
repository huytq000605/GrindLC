package main

import (
	"sort"
	"strings"
)

func groupAnagrams(strs []string) [][]string {
	mapSortedString := make(map[string]int)
	idxResult := 0
	result := [][]string{}
	for _, str := range strs {
		copyArr := strings.Split(str, "")
		sort.Strings(copyArr)
		copyStr := strings.Join(copyArr, "")
		value, ok := mapSortedString[copyStr]
		if ok {
			result[value] = append(result[value], str)
		} else {
			result = append(result, []string{str})
			mapSortedString[copyStr] = idxResult
			idxResult++
		}
	}
	return result
}
