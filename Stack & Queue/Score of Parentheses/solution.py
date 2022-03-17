class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        stack = 0
        current = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack += 1
            else:
                stack -= 1
                if s[i-1] == "(":
                    score += pow(2, stack) 
        return score
