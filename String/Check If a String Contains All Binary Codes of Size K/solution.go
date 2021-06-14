package main

func hasAllCodes(s string, k int) bool {
	theBinaryCodesOfLengthK := 1
	for i := 0; i < k; i++ {
		theBinaryCodesOfLengthK = theBinaryCodesOfLengthK << 1
	}
	binaryMap := make(map[string]bool)
	for i := 0; i < len(s)-k+1; i++ {
		binaryMap[s[i:i+k]] = true
		if len(binaryMap) == theBinaryCodesOfLengthK {
			return true
		}
	}
	return false
}
