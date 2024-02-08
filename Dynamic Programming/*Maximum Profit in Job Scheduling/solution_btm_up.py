class Solution:
    def jobScheduling(self, starts: List[int], ends: List[int], profits: List[int]) -> int:
        n = len(starts)
        jobs = [(starts[i], ends[i], profits[i]) for i in range(n)]
        jobs.sort()
        # dp[i] means the maximum of profit we can get when process range(i, n)
        dp = [0 for _ in range(n)]
        dp[-1] = jobs[-1][2]
        for i in range(n-2, -1, -1):
            start, end = i+1, n
            while start < end:
                mid = start + (end - start) // 2
                if jobs[mid][0] >= jobs[i][1]:
                    end = mid
                else:
                    start = mid + 1
            nxt_job = 0
            if start < n:
                nxt_job = dp[start]
            dp[i] = max(nxt_job + jobs[i][2], dp[i + 1])
        return dp[0]
