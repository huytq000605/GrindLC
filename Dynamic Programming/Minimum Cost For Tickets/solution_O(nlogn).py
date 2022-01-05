class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        @cache
        def dfs(day):
            if day > days[n-1]:
                return 0
            start = 0
            end = n-1
            while start < end:
                mid = start + (end - start) // 2
                if days[mid] < day:
                    start = mid + 1
                else:
                    end = mid
            day = days[start]
            
            trip_length = {0: 1, 1: 7, 2:30}
            result = math.inf
            for trip, cost in enumerate(costs):
                result = min(result, cost + dfs(trip_length[trip] + day))
            return result
        return dfs(0)
