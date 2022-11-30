class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)

        def dfs(idx):
            nonlocal s, n
            sign = "+"
            cur = 0
            stack = []
            
            def update_stack():
                nonlocal sign, cur, stack
                if sign == "+":
                    stack.append(cur)
                elif sign == "-":
                    stack.append(-cur)
                elif sign == "/":
                    stack.append(stack.pop() // cur)
                else:
                    stack.append(stack.pop() * cur)
                
            while idx < n:
                if s[idx].isdigit():
                    cur = cur * 10 + int(s[idx])
                elif s[idx] == "(":
                    cur, idx = dfs(idx + 1)
                elif s[idx] == ")":
                    update_stack()
                    return sum(stack), idx
                elif s[idx] in "+-*/":
                    update_stack()
                    cur, sign = 0, s[idx]
                idx += 1
                
            update_stack()
            return sum(stack)
        return dfs(0)
