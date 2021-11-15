from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s):
            stack = 0
            for l in s:
                if l == "(":
                    stack += 1
                elif l == ")":
                    if stack == 0: return False
                    else: stack -= 1
            return stack == 0
        
        queue = deque([s])
        nextLevel = deque()
        result = []
        seen = set()
        while(queue):
            st = queue.popleft()
            if(isValid(st)):
                result.append(st)
            if len(result) == 0:      
                for i in range(len(st)):
                    if st[i] in "()":
                        newSt = st[0:i] + st[i + 1:]
                        if newSt in seen: continue
                        seen.add(newSt)
                        nextLevel.append(newSt)
            if len(result) == 0 and len(queue) == 0:
                queue, nextLevel = nextLevel, queue
                seen.clear()
        return result