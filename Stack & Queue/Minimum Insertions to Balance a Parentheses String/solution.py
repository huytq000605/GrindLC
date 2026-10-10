class Solution:
    def minInsertions(self, s: str) -> int:
        result = 0
        n = len(s)
        stack = 0
        i = 0
        while i < n:
            if s[i] == '(':
                stack += 1
            else:
                if i+1 >= n or s[i+1] != ')':
                    result += 1
                else:
                    i += 1
                stack -= 1
                if stack < 0:
                    result += 1
                    stack = 0
            i += 1
        return stack*2 + result
            
