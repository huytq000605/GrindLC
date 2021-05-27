package main

/*
Save all freq of vowel into hashmap
Helper is a function that find the longest substring have even numbers of vowel with start as params
Check is function to check if the current string has even numbers of vowel
*/

func findTheLongestSubstring(s string) int {
	result := 0
	vowelMap := make(map[byte]int)
	for i := 0; i < len(s); i++ {
		if s[i] == 117 || s[i] == 101 || s[i] == 111 || s[i] == 97 || s[i] == 105 {
			vowelMap[s[i]] = vowelMap[s[i]] + 1
		}
	}
	for i := 0; i < len(s); i++ {
		length := helper(s, i, vowelMap)
		if result < length {
			result = length
		}
		if s[i] == 117 || s[i] == 101 || s[i] == 111 || s[i] == 97 || s[i] == 105 {
			vowelMap[s[i]] = vowelMap[s[i]] - 1
		}
	}
	return result
}

func helper(s string, start int, vowelMap map[byte]int) int {
	cpyMap := make(map[byte]int)
	for key, value := range vowelMap {
		cpyMap[key] = value
	}

	for end := len(s) - 1; end >= start; end-- {
		if check(cpyMap) {
			return end - start + 1
		}
		if s[end] == 117 || s[end] == 101 || s[end] == 111 || s[end] == 97 || s[end] == 105 {
			cpyMap[s[end]] = cpyMap[s[end]] - 1
		}

	}
	return 0
}

func check(vowelMap map[byte]int) bool {
	for _, value := range vowelMap {
		if value%2 == 1 {
			return false
		}
	}
	return true
}
