class Solution:
    def longestValidParentheses(self, s: str) -> int:
        result = 0
        longest = [0 for i in range(len(s))]
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if len(stack) == 0:
                    continue
                start = stack.pop()
                prev = 0
                if(start - 1 >= 0):
                    prev = longest[start - 1]
                result = max(result, i - start + 1 + prev)
                longest[i] = i - start + 1 + prev
                
        return result