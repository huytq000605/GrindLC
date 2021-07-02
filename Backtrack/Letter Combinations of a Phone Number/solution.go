package main

func letterCombinations(digits string) []string {
	if len(digits) == 0 {
		return []string{}
	}
	result := make([]string, 0)
	digitToLetter := make(map[byte][]string)
	digitToLetter["2"[0]] = []string{"a", "b", "c"}
	digitToLetter["3"[0]] = []string{"d", "e", "f"}
	digitToLetter["4"[0]] = []string{"g", "h", "i"}
	digitToLetter["5"[0]] = []string{"j", "k", "l"}
	digitToLetter["6"[0]] = []string{"m", "n", "o"}
	digitToLetter["7"[0]] = []string{"p", "q", "r", "s"}
	digitToLetter["8"[0]] = []string{"t", "u", "v"}
	digitToLetter["9"[0]] = []string{"w", "x", "y", "z"}
	buildString(digits, 0, digitToLetter, "", &result)
	return result
}

func buildString(digits string, index int, digitToLetter map[byte][]string, current string, result *[]string) {
	if index == len(digits) {
		*result = append(*result, current)
		return
	}
	for _, letter := range digitToLetter[digits[index]] {
		buildString(digits, index+1, digitToLetter, current+letter, result)
	}
}
