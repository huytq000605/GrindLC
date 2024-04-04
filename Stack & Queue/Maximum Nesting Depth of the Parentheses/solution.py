class Solution:
    def maxDepth(self, s: str) -> int:
        stack = 0
        result = 0
        for c in s:
            if c == '(': stack += 1
            elif c == ')': stack -= 1
            result = max(result, stack)
        return result
