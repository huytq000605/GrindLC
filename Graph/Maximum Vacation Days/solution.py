class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        weeks = len(days[0])
        cities = len(flights)
        dp = [-1 for _ in range(cities)]
        dp[0] = 0
        for v in range(cities):
            if flights[0][v]: dp[v] = 0
            flights[v][v] = 1
        for w in range(weeks):
            next_dp = [-1 for _ in range(cities)]
            for u in range(cities):
                if dp[u] < 0: continue
                for v in range(cities):
                    if not flights[u][v]: continue
                    next_dp[v] = max(next_dp[v], dp[u] + days[v][w])
            dp = next_dp
            
        return max(dp)
        
                
                    
        
