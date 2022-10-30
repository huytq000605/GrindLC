class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        n = len(clips)
        dp = [math.inf for i in range(time + 1)]
        dp[0] = 0
        for t in range(1, time + 1):
            for start, end in clips:
                if start <= t <= end:
                    dp[t] = min(dp[t], dp[start] + 1)
            if dp[t] == math.inf: return -1
        return dp[-1]
