class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        result = math.inf
        jobs.sort(reverse = True)
        workers = [0 for i in range(k)]
        def dfs(idx):
            nonlocal result
            if idx >= len(jobs):
                result = min(result, max(*workers, 0))
                return
            seen = set()
            for i, group in enumerate(workers):
                if group in seen: 
                    continue
                seen.add(group)
                if workers[i] + jobs[idx] >= result:
                    continue
                workers[i] += jobs[idx]
                dfs(idx + 1)
                workers[i] -= jobs[idx]
                
        dfs(0)
        return result