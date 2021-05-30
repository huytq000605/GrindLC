package main

func longestPalindromeSubseq(s string) int {
	result := 0
	seen := make(map[string]int)
	for i := 0; i < len(s); i++ {
		odd := helper(s, i, i, seen)
		if result < odd {
			result = odd
		}
		if i != len(s)-1 {
			even := helper(s, i, i+1, seen)
			if result < even {
				result = even
			}
		}
	}
	return result
}

func helper(str string, start int, end int, seen map[string]int) int {
	// key := fmt.Sprintf("%v-%v", start, end)
	key := string(start) + "-" + string(end)
	if value, ok := seen[key]; ok {
		return value
	}
	result := 0
	for start >= 0 && end < len(str) {
		if str[start] == str[end] {
			if start == end {
				result++
			} else {
				result += 2
			}
			start--
			end++
		} else {
			left := helper(str, start-1, end, seen)
			right := helper(str, start, end+1, seen)
			if left > right {
				result += left
			} else {
				result += right
			}
			seen[key] = result
			return result
		}
	}
	seen[key] = result
	return result

}
