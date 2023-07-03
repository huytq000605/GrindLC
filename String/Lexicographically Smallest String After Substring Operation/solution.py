class Solution:
    def smallestString(self, s: str) -> str:
        n = len(s) 
        
        start = 0
        while start < n and s[start] == 'a':
            start += 1
            
        if start == n:
            return s[:n-1] + "z"

        end = start
        for i in range(start, n):
            if s[i] == 'a':
                break
            end = i
        
        new_s = []
        for i, c in enumerate(s):
            if start <= i <= end:
                new_s.append(chr(ord(s[i]) - 1))
            else:
                new_s.append(s[i])
        
            
        return "".join(new_s)
            
