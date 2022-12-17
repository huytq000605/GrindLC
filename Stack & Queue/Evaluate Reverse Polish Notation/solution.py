class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                right = stack.pop()
                left = stack.pop()
                if token == "+":
                    stack.append(left + right)
                elif token == "-":
                    stack.append(left - right)
                elif token == "/":
                    negative = (left * right) < 0
                    left, right = abs(left), abs(right)
                    stack.append(left // right)
                    if negative:
                        stack[-1] = -stack[-1]
                else:
                    stack.append(left * right)
            else:
                stack.append(int(token))
        return stack[0]
