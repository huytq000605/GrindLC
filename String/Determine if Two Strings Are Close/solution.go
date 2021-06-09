package main

/*
So with 2 operations, we need counter(word1) = counter(word2)
*/

func closeStrings(word1 string, word2 string) bool {
	if len(word1) != len(word2) {
		return false
	}
	// 2 freq maps for 2 words
	freq1 := make(map[byte]int)
	freq2 := make(map[byte]int)

	for i := 0; i < len(word1); i++ {
		freq1[word1[i]]++
		freq2[word2[i]]++
	}

	if len(freq1) != len(freq2) {
		return false
	}

	// Check if value array of word1 = value array of word2
	value1Map := make(map[int]int)
	value2 := make([]int, 0)
	for key, val1 := range freq1 {
		val2, ok := freq2[key]
		if !ok {
			return false
		}
		value2 = append(value2, val2)
		value1Map[val1]++
	}
	for i := 0; i < len(value2); i++ {
		if val1 := value1Map[value2[i]]; val1 <= 0 {
			return false
		}
		value1Map[value2[i]]--
	}
	return true

}
