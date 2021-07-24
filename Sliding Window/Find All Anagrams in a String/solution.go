package main

func findAnagrams(s string, p string) []int {
	if len(p) > len(s) {
		return []int{}
	}
	cmp := make([]int, 26)
	ori := make([]int, 26)
	result := make([]int, 0)
	for i := 0; i < len(p); i++ {
		cmp[s[i]-'a']++
		ori[p[i]-'a']++
	}
	start := 0
	if compare(cmp, ori) {
		result = append(result, start)
	}
	start++
	for end := len(p); end < len(s); end, start = end+1, start+1 {
		cmp[s[start-1]-'a']--
		cmp[s[end]-'a']++
		if compare(cmp, ori) {
			result = append(result, start)
		}
	}
	return result
}

func compare(cmp []int, ori []int) bool {
	for i := 0; i <= 25; i++ {
		if cmp[i] != ori[i] {
			return false
		}
	}
	return true
}
