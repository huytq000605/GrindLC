package main

import "strings"

func pushDominoes(dominoes string) string {
	resultArray := append([]string{}, strings.Split("L"+dominoes+"R", "")...)
	j := 0

	for i := 0; i < len(resultArray); i++ {
		if resultArray[i] == "." {
			continue
		}

		if resultArray[i] == "L" {
			if resultArray[j] == "L" {
				for k := j + 1; k < i; k++ {
					resultArray[k] = "L"
				}
			}

			if resultArray[j] == "R" {
				left := j + 1
				right := i - 1
				for left < right {
					resultArray[left] = "R"
					resultArray[right] = "L"
					right--
					left++
				}
			}
			j = i
		}

		if resultArray[i] == "R" {
			if resultArray[j] == "R" {
				for k := j + 1; k < i; k++ {
					resultArray[k] = "R"
				}
			}
			j = i
		}
	}
	result := strings.Join(resultArray[1:len(resultArray)-1], "")
	return result

}
