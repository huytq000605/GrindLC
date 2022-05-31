package main

import "strconv"

func hasAllCodes(s string, k int) bool {
	n := len(s)
	if n < k {
		return false
	}
	goal := 1 << k
	binary := 0
	seen := make(map[int]struct{})
	for i := 0; i < k; i++ {
		binary <<= 1
		last_bit, _ := strconv.Atoi(string(s[i]))
		binary |= last_bit
	}
	seen[binary] = struct{}{}
	for i := k; i < n; i++ {
		binary <<= 1
		binary &^= goal
		last_bit, _ := strconv.Atoi(string(s[i]))
		binary |= last_bit
		seen[binary] = struct{}{}
		if len(seen) == goal {
			return true
		}
	}
	return false
}
