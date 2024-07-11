class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        matching = dict()
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                matching[i] = stack[-1]
                matching[stack.pop()] = i
        
        i = 0
        d = 1
        result = ""
        while i < len(s):
            if i in matching:
                i = matching[i]
                d = -d
            else:
                result += s[i]
            i += d
        return result

