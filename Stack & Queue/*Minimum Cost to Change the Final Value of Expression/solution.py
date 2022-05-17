class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        open_pos = dict()
        n = len(expression)
        
        stack = []
        for i in range(n):
            if expression[i] == "(":
                stack.append(i)
            elif expression[i] == ")":
                open_pos[i] = stack.pop()
        
        def handle_point(v1, c1, v2, c2, op):
            if op == "|":
                if v1 + v2 == 2:
                    return 1, 1 + min(c1, c2)
                if v1 + v2 == 1:
                    return 1, 1
                return 0, min(c1, c2)
            else:
                if v1 + v2 == 2:
                    return 1, min(c1, c2)
                if v1 + v2 == 1:
                    return 0, 1
                return 0, 1 + min(c1, c2)
                    
        
        def dfs(start, end):
            if start == end:
                return (int(expression[start]), 1)
            if expression[end] == ")":
                if open_pos[end] == start:
                    return dfs(start + 1, end - 1)
                else:
                    v1, c1 = dfs(start, open_pos[end] - 2)
                    v2, c2 = dfs(open_pos[end] + 1, end - 1)
                    op = expression[open_pos[end] - 1]
            else:
                v1, c1 = dfs(start, end - 2)
                v2, c2 = int(expression[end]), 1
                op = expression[end - 1]
            return handle_point(v1, c1, v2, c2, op)
        
        return dfs(0, n - 1)[1]