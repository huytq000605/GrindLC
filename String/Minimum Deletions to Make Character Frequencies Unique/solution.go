package main

func minDeletions(s string) int {
	freq := make(map[byte]int)
	for i := 0; i < len(s); i++ {
		freq[s[i]]++
	}
	result := 0
	valueMap := make(map[int]bool)
	for _, value := range freq {
		for {
			_, ok := valueMap[value]
			if ok {
				value--
				result++
			} else {
				break
			}
		}
		if value != 0 {
			valueMap[value] = true
		}
	}
	return result

}
