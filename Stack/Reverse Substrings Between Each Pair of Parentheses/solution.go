package main

func reverseParentheses(s string) string {
	result := s
	stack := []int{}
	for i := 0; i < len(result); i++ {
		if result[i] == 40 {
			stack = append(stack, i)
		}
		if result[i] == 41 {
			start := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			result = result[:start] + reverse(result[start+1:i]) + result[i+1:]
			i -= 2
		}
	}
	return result
}

func reverse(s string) string {
	result := ""
	for i := len(s) - 1; i >= 0; i-- {
		result += string(s[i])
	}
	return result
}
