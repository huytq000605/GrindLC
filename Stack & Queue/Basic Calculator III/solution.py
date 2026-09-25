class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        ops = []
        stack = []
        i = 0
        def ope():
            sign = ops.pop()
            r, l = stack.pop(), stack.pop()
            if sign == "+":
                stack.append(l+r)
            elif sign == "-":
                stack.append(l-r)
            elif sign == "*":
                stack.append(l*r)
            elif sign == "/":
                negative = l * r < 0
                stack.append(abs(l) // abs(r))
                if negative: stack[-1] = -stack[-1]
            
        while i < n:
            ch = s[i]
            if ch in "+-*/":
                while ops and \
                    not (ops[-1] in "()" or (ops[-1] in "+-" and ch in "*/")):
                    ope()
                ops.append(ch)
            elif ch == "(":
                ops.append("(")
            elif ch == ")":
                while ops and ops[-1] != "(":
                    ope()
                ops.pop()
                if ops and ops[-1] == "-":
                    stack[-1] = -stack[-1]
                    ops[-1] = "+"
            else:
                num = int(s[i])
                while i+1 < n and s[i+1].isdigit():
                    i += 1
                    num = num * 10 + int(s[i])
                stack.append(num)
            i += 1
        while ops:
            ope()
        return stack[-1]
