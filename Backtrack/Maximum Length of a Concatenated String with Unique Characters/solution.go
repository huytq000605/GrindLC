package main

import "errors"

func maxLength(arr []string) int {
	return buildString(arr, 0, "", make(map[byte]bool))
}

func buildString(arr []string, index int, currentString string, currentSet map[byte]bool) int {
	if index == len(arr) {
		return len(currentString)
	}
	result := len(currentString)
	for i := index; i < len(arr); i++ {
		err := addToSet(currentSet, arr[i])
		if err != nil {
			continue
		}
		res := buildString(arr, i+1, currentString+arr[i], currentSet)
		if res > result {
			result = res
		}
		removeFromSet(currentSet, arr[i])
	}
	return result
}

func addToSet(set map[byte]bool, s string) error {
	for i := range s {
		if _, ok := set[s[i]]; ok {
			for j := 0; j < i; j++ {
				delete(set, s[j])
			}
			return errors.New("Had this letter")
		}
		set[s[i]] = true
	}
	return nil
}

func removeFromSet(set map[byte]bool, s string) {
	for i := range s {
		delete(set, s[i])
	}
}
