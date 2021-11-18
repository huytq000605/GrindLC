class Solution:
    def calculate(self, s: str) -> int:
        def dfs(idx):
            stack = []
            current = 0
            sign = "+"
            
            def updateStack():
                nonlocal sign
                nonlocal current
                nonlocal stack
                if sign == "+":
                    stack.append(current)
                elif sign == "-":
                    stack.append(-current)
                elif sign == "*":
                    stack.append(stack.pop() * current)
                else:
                    stack.append(stack.pop() // current)
            
            while idx < len(s):
                if s[idx].isdigit():
                    current = current * 10 + int(s[idx])
                elif s[idx] == "(":
                    num, nextIdx = dfs(idx + 1)
                    current = num
                    idx = nextIdx
                elif s[idx] == ")":
                    updateStack()
                    return sum(stack), idx
                elif s[idx] in "+-*/":
                    updateStack()
                    current = 0
                    sign = s[idx]
                idx += 1
            updateStack()
            return sum(stack)
        return dfs(0)
                    