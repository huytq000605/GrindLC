class Solution:
    def parseTernary(self, exp: str) -> str:
        n = len(exp)
        stack = []
        i = n-1
        while i >= 0:
            if exp[i] not in ":?":
                stack.append(exp[i])
            elif exp[i] == "?":
                i -= 1
                first = stack.pop()
                second = stack.pop()
                if exp[i] == "T": 
                    stack.append(first)
                else:
                    stack.append(second)
            i -= 1
        return stack[-1]
