/*
let map store condition ( apply for more question)
if still fit condition then increase
at this question, for each fit condition, we can get [from end to last] substring
*/

func numberOfSubstrings(s string) int {
	idxMap := make(map[byte]int)
	for i := byte('a'); i <= byte('c'); i++ {
		idxMap[i] = 0
	}
	start := 0
	result := 0
	for end := 0; end < len(s); end++ {
		idxMap[s[end]] = idxMap[s[end]] + 1
		for isFullfilled(idxMap) {
			result += len(s) - 1 - end + 1
			idxMap[s[start]] = idxMap[s[start]] - 1
			start++
		}
	}
	return result
}

func isFullfilled(idxMap map[byte]int) bool {
	for _, value := range idxMap {
		if value == 0 {
			return false
		}
	}
	return true
}