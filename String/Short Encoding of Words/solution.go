package main

import "sort"

func minimumLengthEncoding(words []string) int {
	stringMap := make(map[string]bool)
	result := ""
	sort.Slice(words, func(i, j int) bool {
		return len(words[j]) < len(words[i])
	})
	for _, word := range words {
		if _, ok := stringMap[word]; ok {
			continue
		}
		for i := 0; i < len(word); i++ {
			stringMap[word[i:]] = true
		}
		result += word + "#"
	}
	return len(result)
}
