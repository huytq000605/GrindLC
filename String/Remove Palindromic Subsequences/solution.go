package main

func removePalindromeSub(s string) int {
	if len(s) == 0 {
		return 0
	}
	isPalindrome := true
	i, j := 0, len(s)-1
	for i < j {
		if s[i] != s[j] {
			isPalindrome = false
			break
		}
		i += 1
		j -= 1
	}
	if isPalindrome {
		return 1
	} else {
		return 2
	}
}
