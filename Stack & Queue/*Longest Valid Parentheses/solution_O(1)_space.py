class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        result = 0
        
        stack = 0
        total = 0
        for i in range(n):
            if s[i] == "(":
                stack += 1
            else:
                stack -= 1
                total += 2
                if stack < 0:
                    stack = 0
                    total = 0
            if stack == 0:
                result = max(result, total)
        
        stack = 0
        total = 0
        for i in range(n-1, -1, -1):
            if s[i] == ")":
                stack += 1
            else:
                stack -= 1
                total += 2
                if stack < 0:
                    stack = 0
                    total = 0
            if stack == 0:
                result = max(result, total)
        return result
