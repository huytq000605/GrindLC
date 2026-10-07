class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = 0
        result = 0
        for c in s:
            if c == "(":
                stack += 1
            elif c == ")":
                stack -= 1
            if stack < 0:
                stack = 0
                result += 1
        return result + stack
