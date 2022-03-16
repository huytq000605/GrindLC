class Solution:
    def longestPrefix(self, s: str) -> str:
        left = 0
        right = 0
        n = len(s)
        result = 0
        MOD = 2**31 - 1
        for i in range(n - 1):
            letter_left = ord(s[i]) - ord('a') + 1
            letter_right = ord(s[n-1-i]) - ord('a') + 1
            
            left *= 26
            left += letter_left
            left %= MOD
            
            mutiply = pow(26, i, MOD)
            right += letter_right * mutiply
            right %= MOD    
            
            if left == right:
                result = i + 1
        if result == 0:
            return ""
        return s[:result]