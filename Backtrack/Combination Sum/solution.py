class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        current = []
        current_sum = 0
        def dfs(idx):
            nonlocal result, current, current_sum
            if current_sum == target:
                result.append([*current])
            if idx >= len(candidates):
                return
            for i in range(idx, len(candidates)):
                if current_sum + candidates[i] <= target:
                    current_sum += candidates[i]
                    current.append(candidates[i])
                    dfs(i)
                    current.pop()
                    current_sum -= candidates[i]
        dfs(0)
        return result