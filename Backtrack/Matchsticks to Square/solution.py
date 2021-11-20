class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sumSticks = sum(matchsticks)
        matchsticks.sort(reverse = True)
        if sumSticks % 4 != 0:
            return False
        target = sumSticks // 4
        states = [0,0,0,0]
        def dfs(idx):
            if idx >= len(matchsticks):
                return True
            seen = set()
            for i, state in enumerate(states):
                if state in seen:
                    continue
                seen.add(state)
                if state + matchsticks[idx] <= target:
                    states[i] += matchsticks[idx]
                    if(dfs(idx + 1)): return True
                    states[i] -= matchsticks[idx]
                    
            return False
        return dfs(0)