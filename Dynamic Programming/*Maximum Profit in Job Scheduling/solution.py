class Solution:
    def jobScheduling(self, starts: List[int], ends: List[int], profits: List[int]) -> int:
        n = len(starts)
        jobs = [(starts[i], ends[i], profits[i]) for i in range(n)]
        jobs.sort()
        @cache
        def dfs(i):
            if i >= n:
                return 0
            result = dfs(i+1)
            # j as the index of the next job
            # jobs[j][0] >= ends[i]
            start = i + 1
            end = n
            while start < end:
                mid = start + (end - start) // 2
                if jobs[mid][0] >= jobs[i][1]:
                    end = mid
                else:
                    start = mid + 1
            result = max(result, dfs(start) + jobs[i][2])
            return result
        return dfs(0)
