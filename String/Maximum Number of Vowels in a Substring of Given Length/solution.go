package main

func maxVowels(s string, k int) int {
	count := 0
	for i := 0; i < k; i++ {
		ch := s[i]
		if ch == 97 || ch == 101 || ch == 105 || ch == 111 || ch == 117 {
			count++
		}
	}
	result := count
	for i := k; i < len(s); i++ {
		ch := s[i]
		if ch == 97 || ch == 101 || ch == 105 || ch == 111 || ch == 117 {
			count++
		}
		ch = s[i-k]
		if ch == 97 || ch == 101 || ch == 105 || ch == 111 || ch == 117 {
			count--
		}
		if count > result {
			result = count
		}
	}
	return result
}
