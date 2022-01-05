class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        trip_length = {0: 1, 1: 7, 2:30}
        @cache
        def dfs(idx):
            if idx >= n:
                return 0
            result = math.inf
            next_idx = idx
            for trip, cost in enumerate(costs):
                while next_idx < n and days[next_idx] < days[idx] + trip_length[trip]:
                    next_idx += 1
                result = min(result, cost + dfs(next_idx))
            return result
        return dfs(0)
