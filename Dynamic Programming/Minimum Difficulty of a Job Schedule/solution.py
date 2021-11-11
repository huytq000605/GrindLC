class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @lru_cache(None)
        def dfs(idx, day):
            if(idx >= len(jobDifficulty) and day >= d):
                return 0
            if idx >= len(jobDifficulty):
                return math.inf
            if day >= d:
                return math.inf
            difficult = 0
            result = math.inf
            for i in range(idx, len(jobDifficulty)):
                difficult = max(difficult, jobDifficulty[i])
                result = min(result, difficult + dfs(i + 1, day + 1))
            return result
        ans = dfs(0, 0)
        if ans >= math.inf:
            return -1
        return ans