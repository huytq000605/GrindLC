class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        invalidOpen = 0
        invalidClose = 0
        stack = 0
        for l in s:
            if l == ")":
                if stack == 0: invalidClose += 1
                else: stack -= 1
            if l == "(":
                stack += 1
        invalidOpen = stack
        
        result = set()
        
        def dfs(idx, invalidOpen, invalidClose, stack, current):
            if invalidOpen < 0 or invalidClose < 0 or stack < 0:
                return
            if idx >= len(s):
                if invalidOpen == 0 and invalidClose == 0 and stack == 0:
                    result.add(current)
                    return
                else:
                    return

            if s[idx] == ")":
                dfs(idx + 1, invalidOpen, invalidClose - 1, stack, current)
                dfs(idx + 1, invalidOpen, invalidClose, stack - 1, current + s[idx])
            elif(s[idx] == "("):
                dfs(idx + 1, invalidOpen - 1, invalidClose, stack, current)
                dfs(idx + 1, invalidOpen, invalidClose, stack + 1, current + s[idx])
            else:
                dfs(idx + 1, invalidOpen, invalidClose, stack, current + s[idx])
                
        
        dfs(0, invalidOpen, invalidClose, 0, "")
        return list(result)
                
                    
                    