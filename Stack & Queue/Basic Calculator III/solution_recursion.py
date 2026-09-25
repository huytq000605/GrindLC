class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        def handle_sign(sign, stack, cur):
            if sign == "+":
                stack.append(cur)
            elif sign == "-":
                stack.append(-cur)
            elif sign == "*":
                stack.append(stack.pop() * cur)
            elif sign == "/":
                negative = stack[-1] * cur < 0
                stack.append(abs(stack.pop()) // abs(cur))
                if negative: stack[-1] = -stack[-1]


        def dfs(i):
            stack = []
            cur = 0
            sign = "+"
            while i < n:
                c = s[i]
                if c.isdigit():
                    cur = cur * 10 + int(c)
                elif c in "+-*/":
                    handle_sign(sign, stack, cur)
                    sign = c
                    cur = 0
                elif c == "(":
                    end_idx, num = dfs(i+1)
                    cur = num
                    i = end_idx
                elif c == ")":
                    handle_sign(sign, stack, cur)
                    return i, sum(stack)
                i += 1
            handle_sign(sign, stack, cur)
            return sum(stack)
        return dfs(0)
