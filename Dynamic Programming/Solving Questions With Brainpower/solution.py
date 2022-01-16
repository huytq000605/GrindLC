class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def dfs(idx):
            if idx >= len(questions):
                return 0
            solve = questions[idx][0] + dfs(idx + questions[idx][1] + 1)
            skip = dfs(idx + 1)
            return max(solve, skip)
        return dfs(0)