package main

type keyfreq struct {
	key  byte
	freq int
}

func removeDuplicates(s string, k int) string {
	stack := make([]keyfreq, 0)
	for i := 0; i < len(s); i++ {
		if len(stack) > 0 && s[i] == stack[len(stack)-1].key {
			stack[len(stack)-1].freq++
		} else {
			stack = append(stack, keyfreq{s[i], 1})
		}

		if stack[len(stack)-1].freq == k {
			stack = stack[0 : len(stack)-1]
		}

	}
	result := make([]byte, 0)
	for _, ele := range stack {
		for i := 0; i < ele.freq; i++ {
			result = append(result, ele.key)
		}
	}
	return string(result)
}
