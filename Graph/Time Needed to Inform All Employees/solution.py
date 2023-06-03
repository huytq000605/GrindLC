class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        reports = [[] for _ in range(n)]
        for report, manager in enumerate(manager):
            if manager == -1: continue
            reports[manager].append(report)
        
        def dfs(manager):
            result = 0
            for report in reports[manager]:
                result = max(result, informTime[report] + dfs(report))
            return result
        return dfs(headID) + informTime[headID]
