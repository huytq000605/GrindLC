class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current = 0
        sign = "+"
        for i in range(len(s)):
            if s[i].isdigit():
                current = current * 10 + int(s[i])
            if s[i] in "+-*/" or i == len(s) - 1:
                if(sign == "+"):
                    stack.append(current)
                elif(sign == "-"):
                    stack.append(-current)
                elif(sign == "/"):
                    stack.append(int(stack.pop() / current))
                elif(sign == "*"):
                    stack.append(stack.pop() * current)
                current = 0
                sign = s[i]
            
        return sum(stack)
        
                