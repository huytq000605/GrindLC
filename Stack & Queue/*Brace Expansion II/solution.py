class Solution:
    def braceExpansionII(self, expr: str) -> list[str]:
        n = len(expr)
        stack = []
        ops = []
        def ope():
            r, l = stack.pop(), stack.pop()
            result = set()
            op = ops.pop()
            if op == "*":
                for ll in l:
                    for rr in r:
                        result.add(ll + rr)
            elif op == "+":
                result = l | r
            stack.append(result)
            return result  
        
        for i, ch in enumerate(expr):
            if ch == ',':
                while ops and ops[-1] == "*":
                    ope()
                ops.append("+")
            elif ch == '{':
                if i > 0 and (expr[i-1] == '}' or expr[i-1].isalpha()):
                    ops.append("*")
                ops.append('{')
            elif ch == '}':
                while ops[-1] != '{':
                    ope()
                ops.pop()
            else:
                if i > 0 and (expr[i-1] == '}' or expr[i-1].isalpha()):
                    ops.append("*")
                stack.append({ch})
        
        while ops:
            ope()
        return sorted(stack[-1])

                

