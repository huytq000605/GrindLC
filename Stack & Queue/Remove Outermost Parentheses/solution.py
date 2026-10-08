class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        st = 0
        for c in s:
            if c == "(": 
                st += 1
                if st > 1: result += c
            else: 
                st -= 1
                if st: result += c
        return result
