package main

func maxUniqueSplit(s string) int {
	return split(s, 0, make(map[string]bool))
}

func split(s string, start int, used map[string]bool) int {
	if start == len(s) {
		return len(used)
	}
	result := 0
	for i := start; i < len(s); i++ {
		beUsedString := s[start : i+1]
		if _, ok := used[beUsedString]; !ok {
			used[beUsedString] = true
			res := split(s, i+1, used)
			if res > result {
				result = res
			}
			delete(used, beUsedString)
		}
	}
	return result
}
