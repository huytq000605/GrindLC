func minimumDeletions(s string) int {
	prefixA := make([]int, len(s))
	prefixB := make([]int, len(s))
	totalA := 0
	totalB := 0

	for i := 0; i < len(s); i++ {
		if i == 0 {
			if s[i] == 'a' {
				prefixA[0] = 1
				totalA++
			} else {
				prefixB[0] = 1
				totalB++
			}
		} else {
			if s[i] == 'a' {
				prefixA[i] = prefixA[i-1] + 1
				prefixB[i] = prefixB[i-1]
				totalA++
			} else {
				prefixA[i] = prefixA[i-1]
				prefixB[i] = prefixB[i-1] + 1
				totalB++
			}
		}
	}

	result := 0
	if totalA > totalB {
		result = totalB
	} else {
		result = totalA
	}

	for firstB := 1; firstB < len(s); firstB++ {
		leftDelete := prefixB[firstB-1]
		rightDelete := totalA - prefixA[firstB]
		res := leftDelete + rightDelete
		if res < result {
			result = res
		}
	}

	return result
}