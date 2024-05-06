class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        cur = []
        result = []
        def dfs(i, s):
            nonlocal result, cur, candidates, target
            if s > target: return
            if i >= len(candidates):
                if s == target:
                    result.append([*cur])
                return
            cur.append(candidates[i])
            dfs(i+1, s + candidates[i])
            cur.pop()
            j = i+1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            dfs(j, s)
        dfs(0, 0)
        return result
