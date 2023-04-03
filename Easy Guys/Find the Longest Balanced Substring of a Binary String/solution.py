class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        result = 0
        zeros = 0
        ones = 0
        for c in s:
            if c == "0":
                if ones: zeros = 0
                zeros += 1
                ones = 0
            else:
                ones += 1
            result = max(result, min(ones, zeros) * 2)
        return result
                
        
