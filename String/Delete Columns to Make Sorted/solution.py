class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0
        m, n = len(strs), len(strs[0])
        for c in range(n):
            sort = True
            for r in range(m-1):
                if strs[r][c] > strs[r+1][c]:
                    sort = False
                    break
            if not sort:
                result += 1
        return result
