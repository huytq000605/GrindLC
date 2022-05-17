class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        best = [math.inf for i in range(numLaps + 1)]
        
        for tire in tires:
            f, r = tire
            current = f
            total = current
            for lap in range(1, numLaps + 1):
                best[lap] = min(best[lap], total)
                if (current * r - current) >= (changeTime + f*r):
                    break
                current *= r
                total += current
        
        # dp[i] = Minimum time to finish first i laps 
        dp = [0] + [math.inf for i in range(numLaps)]
        
        # Has gone through i laps
        for i in range(numLaps+1):
            # Try to go j steps
            for j in range(1, numLaps + 1):
                # Out of laps or can't go further from i
                if i + j > numLaps or best[j] == math.inf:
                    break
                if i == 0:
                    dp[i+j] = min(dp[i+j], best[j])
                else:
                    dp[i+j] = min(dp[i+j], dp[i] + changeTime + best[j])
        return dp[numLaps]