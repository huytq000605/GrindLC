package main

func letterCombinations(digits string) []string {
	if len(digits) == 0 {
		return []string{}
	}
	result := make([]string, 0)
	digitToLetter := make(map[byte][]string)
	digitToLetter['2'] = []string{"a", "b", "c"}
	digitToLetter['3'] = []string{"d", "e", "f"}
	digitToLetter['4'] = []string{"g", "h", "i"}
	digitToLetter['5'] = []string{"j", "k", "l"}
	digitToLetter['6'] = []string{"m", "n", "o"}
	digitToLetter['7'] = []string{"p", "q", "r", "s"}
	digitToLetter['8'] = []string{"t", "u", "v"}
	digitToLetter['9'] = []string{"w", "x", "y", "z"}
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
