class Solution:
    def countTexts(self, keys: str) -> int:
        n = len(keys)
        @cache
        def dfs(i):
            if i >= n:
                return 1
            result = 0
            for j in range(0, 4):
                if i + j >= n or keys[i+j] != keys[i] or (j == 3 and keys[i] not in ["7","9"]):
                    break
                result += dfs(i + j + 1)
            return result % (10**9+7)
        return dfs(0)