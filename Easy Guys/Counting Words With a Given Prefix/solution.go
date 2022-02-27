package main

func prefixCount(words []string, pref string) int {
	result := 0
	for _, word := range words {
			if len(word) < len(pref) {
					continue
			}
			match := 1
			for i := 0; i < len(pref); i++ {
					if pref[i] != word[i] {
							match = 0
							break
					}
			}
			result += match
	}
	return result
}