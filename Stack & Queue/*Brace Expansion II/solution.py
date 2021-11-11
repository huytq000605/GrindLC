class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        result = set()
        def dfs(idx, current, stack):
            nonlocal result
            for i in range(idx, len(current)):
                if current[i] == "{":
                    stack.append(i)
                elif current[i] == "}":
                    start = stack.pop()
                    selections = current[start + 1: i].split(",")
                    for selection in selections:
                        newCurrent = current[0:start] + selection + current[i+1:]
                        dfs(start + len(selection), newCurrent, [*stack])
                    return
            result.add(current)
        
        dfs(0, expression, [])
        
        finalResult = set()
        for res in result:
            res = res.split(",")
            for r in res: finalResult.add(r)
            
        finalResult = sorted(list(finalResult))
        
        return finalResult