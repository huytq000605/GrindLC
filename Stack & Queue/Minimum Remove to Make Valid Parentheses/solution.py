class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        total_open = 0
        skip_last_open = 0
        for l in s:
            if l == "(":
                total_open += 1
                skip_last_open += 1
            elif l == ")":
                if skip_last_open == 0:
                    continue
                skip_last_open -= 1
        
        current_open = 0    
        result = ""
        stack = 0
        for l in s:
            if l == "(":
                if total_open - current_open <= skip_last_open:
                    continue
                current_open += 1
                
                stack += 1
            elif l == ")":
                if stack == 0:
                    continue
                stack -= 1
            result += l
        
        return result