class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        current = ""
        for l in path:
            if l == "/":
                if current == "..":
                    if stack: stack.pop()
                elif current not in " .":
                    stack.append(current)
                current = ""
            else:
                current += l
                
        if current == "..":
            if stack: stack.pop()
        elif current not in " .":
            stack.append(current)
        
        return "/" + "/".join(stack)