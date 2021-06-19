package main

import "strings"

func maximumBinaryString(binary string) string {
	leadingOnes := strings.Index(binary, "0")
	zeros := strings.Count(binary, "0")
	if zeros == 0 {
		return binary
	}
	result := strings.Repeat("1", len(binary))
	result = result[:leadingOnes+zeros-1] + "0" + result[leadingOnes+zeros:]
	return result
}
