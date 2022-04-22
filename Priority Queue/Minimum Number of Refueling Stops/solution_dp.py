class Solution:
    def minRefuelStops(self, target: int, fuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        # dp[i] = farest can go with i stop
        dp = [fuel] + [0 for i in range(n)]
        for i in range(n):
            for j in range(i, -1, -1):
                if dp[j] >= stations[i][0]:
                    dp[j+1] = max(dp[j+1], dp[j] + stations[i][1])
        for i in range(n + 1):
            if dp[i] >= target:
                return i
        return -1
        