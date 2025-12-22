class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        @cache
        def dfs(i, j):
            if i >= len(strs[0]): return 0
            valid = True
            for s in range(len(strs)):
                if j != -1 and strs[s][i] < strs[s][j]:
                    valid = False
                    break
            if not valid:
                return dfs(i+1, j) + 1
            else:
                return min(dfs(i+1, i), dfs(i+1, j) + 1)
        return dfs(0, -1)
