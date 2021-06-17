package main

func smallestSubsequence(s string) string {
	last := [26]int{}
	stack := ""
	seen := make(map[byte]bool)
	for index, letter := range s { // save last index of each character in s
		last[letter-'a'] = index
	}
	for i := 0; i < len(s); i++ {
		letter := s[i]
		if _, ok := seen[letter]; ok { // Not getting the dupplicate characters
			continue
		}
		for len(stack) > 0 && letter < stack[len(stack)-1] && i < last[stack[len(stack)-1]-'a'] { // If current letter is lower than the previous one and the previous one still can get after => delete the previous one
			delete(seen, stack[len(stack)-1])
			stack = stack[:len(stack)-1]
		}
		stack += string(letter)
		seen[letter] = true
	}
	return stack
}
