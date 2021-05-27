package main

import "strings"

/*
Save all word in dictionary in a hashmap
Split the setence by space, for each word, we check if the substring from 0 to n in hashmap, we replace it then break ( we got shortest substring here)
Tweak: save the min & max word of dict to decrease number of loop when checking
Note: can be implement in trie for (better performance?)
*/

func replaceWords(dictionary []string, sentence string) string {
	arrStr := strings.Split(sentence, " ")
	hashmap := make(map[string]bool)
	min, max := 1000, 0
	for _, word := range dictionary {
		if len(word) > max {
			max = len(word)
		}
		if len(word) < min {
			min = len(word)
		}
		hashmap[word] = true
	}
	for idx, word := range arrStr {
		for i := min; i < max+1 && i < len(word); i++ {
			if _, ok := hashmap[word[:i]]; ok {
				arrStr[idx] = word[:i]
				break
			}
		}
	}
	result := strings.Join(arrStr, " ")
	return result
}
