class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        i = 0
        while i < len(expression):
            if(expression[i] == "("):
                stack.append(i)
            elif(expression[i] == ")"):
                start = stack.pop()
                operator = expression[start - 1]
                values = expression[start + 1:i].split(",")
                replace = ""
                if operator == "!":
                    if values[0] == "t":
                        replace = "f"
                    else:
                        replace = "t"
                elif operator == "&":
                    if "f" in values:
                        replace = "f"
                    else:
                        replace = "t"
                else:
                    if "t" in values:
                        replace = "t"
                    else:
                        replace = "f"
                expression = expression[0:start - 1] + replace + expression[i + 1:]
                i = start - 2 + len(replace)
            i += 1
        return expression == "t"