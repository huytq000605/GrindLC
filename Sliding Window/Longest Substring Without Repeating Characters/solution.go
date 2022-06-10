package main

func lengthOfLongestSubstring(s string) int {
	seen := make(map[byte]struct{})
	result, start := 0, 0
	for i := range s {
		for {
			if _, ok := seen[s[i]]; ok {
				delete(seen, s[start])
				start += 1
			} else {
				break
			}
		}
		if i-start+1 > result {
			result = i - start + 1
		}
		seen[s[i]] = struct{}{}
	}
	return result
}
