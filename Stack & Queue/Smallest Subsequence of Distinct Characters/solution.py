class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = dict()
        for i in range(len(s)):
            last[s[i]] = i
        result = ""
        for i in range(len(s)):
            c = s[i]
            while result and c not in result and c < result[-1] and last[result[-1]] > i:
                result = result[:-1]
            if c not in result:
                result += c
            
        return result        
