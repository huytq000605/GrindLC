class Solution:
    def clumsy(self, n: int) -> int:
        sign = "+"
        signs = ["*", "/", "+", "-"]
        idxSign = 0
        current = n
        stack = []
        i = 0
        def update_stack():
            if sign == "+":
                stack.append(current)
            elif sign == "-":
                stack.append(-current)
            elif sign == "*":
                stack.append(stack.pop() * current)
            else:
                if stack[-1] < 0:
                    stack.append(math.ceil(stack.pop() / current))
                else:
                    stack.append(stack.pop() // current)
            
        while n > 0:
            if i % 2 == 0:
                current = n
                n -= 1
            else:
                update_stack()
                sign = signs[idxSign]
                idxSign = (idxSign + 1) % 4
            i += 1
        update_stack()
        return sum(stack)