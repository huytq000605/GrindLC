/*
So basically, if 2 string has x is longest common subsequence, so we append string1 a char, append string2 a char. If two characters we append for string1 and string2 was the same => x + 1 is longest common subsequence but if its not, then the the longest common subsequence will be MAX of LCS(string1, new string2) and LCS(new string1, string 2)
*/

func longestCommonSubsequence(text1 string, text2 string) int {
	dp := make([][]int, len(text1)+1)
	for i := range dp {
		dp[i] = make([]int, len(text2)+1)
	}
	for i := 1; i < len(dp); i++ {
		for j := 1; j < len(dp[0]); j++ {
			if text1[i-1] == text2[j-1] {
				dp[i][j] = dp[i-1][j-1] + 1
			} else {
				if dp[i-1][j] >= dp[i][j-1] {
					dp[i][j] = dp[i-1][j]
				} else {
					dp[i][j] = dp[i][j-1]
				}
			}
		}
	}
	return dp[len(dp)-1][len(dp[0])-1]
}