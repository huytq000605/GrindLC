# Backtrack with pruning
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        dp = [dict() for i in range(len(tasks))]
        result = math.inf
        states = []
        def dfs(taskIdx):
            nonlocal result
            if taskIdx >= len(tasks):
                result = min(result, len(states))
                return len(states)
            key = str(sorted(states)) # Sorted Array to be state
            if key in dp[taskIdx]:
                return dp[taskIdx][key]
            
            seen = set()
            res = math.inf
            for i, state in enumerate(states):
                if state in seen or state + tasks[taskIdx] > sessionTime:
                    continue
                seen.add(state)
                states[i] += tasks[taskIdx]
                res = min(res, dfs(taskIdx + 1))
                states[i] -= tasks[taskIdx]
            
            if len(states) + 1 < result:
                states.append(tasks[taskIdx])
                res = dfs(taskIdx + 1)
                states.pop()
            
            dp[taskIdx][key] = res
            return res
        dfs(0)
        return result
                        