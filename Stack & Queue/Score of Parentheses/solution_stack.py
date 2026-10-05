class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for c in s:
            if c == "(":
                stack.append(0)
            else:
                v = stack.pop()
                u = stack.pop()
                stack.append(u + max(1, v*2))
        return stack[0]
