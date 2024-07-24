class Solution:
    def getSmallestString(self, s: str) -> str:
        for i in range(len(s) - 1):
            if s[i] > s[i+1] and (ord(s[i]) - ord(s[i+1])) & 1 == 0:
                return s[:i] + s[i+1] + s[i] + s[i+2:]
        return s
            
