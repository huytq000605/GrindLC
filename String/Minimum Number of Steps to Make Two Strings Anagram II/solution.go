func minSteps(s string, t string) int {
	count := make([]int, 26)
	for _, c := range s {
			count[c - 'a'] += 1
	}
	for _, c := range t {
			count[c - 'a'] -= 1
	}
	result := 0
	for _, c := range count {
			result += int(math.Abs(float64(c)))
	}
	return result
}