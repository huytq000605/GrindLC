class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        intervals = sorted([(startTime[i], endTime[i], profit[i]) for i in range(n)])
        @cache
        def dfs(i):
            if i >= n:
                return 0
            result = dfs(i+1)
            start = i+1
            end = n
            while start < end:
                mid = start + (end - start) // 2
                if intervals[mid][0] < intervals[i][1]:
                    start = mid + 1
                else:
                    end = mid
            result = max(result, intervals[i][2] + dfs(start))
            return result
        return dfs(0)
