# Time Complexity: 2 ^ len(tasks) * sessionTime
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        @lru_cache(None)
        def dfs(taskState, remain):
            if taskState == (1 << len(tasks)) - 1:
                return 0
            result = math.inf
            for i in range(len(tasks)):
                if (taskState >> i) & 1 == 1:
                    continue
                newMask = taskState | (1 << i)
                if tasks[i] <= remain:
                    result = min(result, dfs(newMask, remain - tasks[i]))
                else:
                    result = min(result, 1 + dfs(newMask, sessionTime - tasks[i]))
            return result
        return dfs(0, sessionTime) + 1
        