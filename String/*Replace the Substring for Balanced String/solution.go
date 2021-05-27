func balancedString(s string) int {
	// Caculate frequency of each letter in s
	oriFreq := make(map[byte]int)
	oriFreq[byte('Q')] = 0
	oriFreq[byte('W')] = 0
	oriFreq[byte('E')] = 0
	oriFreq[byte('R')] = 0
	for i := range s {
		oriFreq[s[i]] = oriFreq[s[i]] + 1
	}

	// we stored a map contains frequency of each letter we need in our string to a map
	needToMeet := make(map[byte]int)
	for key, value := range oriFreq {
		needToMeet[key] = value - len(s)/4
	}
	if isFullfilled(needToMeet) {
		return 0
	}

	start := 0
	result := 999999
	for end := range s {
		needToMeet[s[end]] = needToMeet[s[end]] - 1
		for isFullfilled(needToMeet) { // Try to find the shortest one
			if end-start+1 < result {
				result = end - start + 1
			}
			needToMeet[s[start]] = needToMeet[s[start]] + 1
			start++
		}
	}

	return result

}

// If we've already meet all letter we need
func isFullfilled(needToMeet map[byte]int) bool {
	for _, value := range needToMeet {
		if value > 0 {
			return false
		}
	}
	return true
}