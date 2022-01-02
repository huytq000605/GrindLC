class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        states = []
        def dfs(idx, current):
            if idx >= n:
                if len(states) >= 2 and current == -1:
                    return True
                else:
                    return False
            if current == - 1:
                current = int(s[idx])
            else:
                current = current * 10 + int(s[idx])
            if len(states) > 0 and current >= states[-1]:
                return False
            if len(states) == 0 or current + 1 == states[-1]:
                states.append(current)
                if dfs(idx + 1, -1):
                    return True
                states.pop()
            return dfs(idx + 1, current)
        
        return dfs(0, -1)
