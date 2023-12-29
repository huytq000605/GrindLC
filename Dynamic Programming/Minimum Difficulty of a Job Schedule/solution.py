class Solution:
    def minDifficulty(self, ds: List[int], d: int) -> int:
        if len(ds) < d:
            return -1
        @cache
        def dfs(job, day):
            if job >= len(ds) and day >= d:
                return 0
            if job >= len(ds): return math.inf
            if day >= d: return math.inf
            mx = 0
            result = math.inf
            # doing from day to d
            for end_job in range(job, len(ds)): 
                mx = max(mx, ds[end_job])
                result = min(result, dfs(end_job + 1, day + 1) + mx)
            return result
        return dfs(0, 0)
