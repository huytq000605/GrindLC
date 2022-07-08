from functools import cache

class Solution:
    def minCost(self, houses: List[int], costs: List[List[int]], m: int, n: int, target: int) -> int:
        @cache
        def dfs(house, neighborhoods, previous):
            if house >= m:
                if neighborhoods == target:
                    return 0
                else:
                    return math.inf
            if houses[house] != 0:
                if houses[house] != previous:
                    neighborhoods += 1
                return dfs(house + 1, neighborhoods, houses[house])
            else:
                result = math.inf
                for idx, cost in enumerate(costs[house]):
                    color = idx + 1
                    new_neighborhoods = neighborhoods
                    if color != previous:
                        new_neighborhoods += 1
                    result = min(result, cost + dfs(house + 1, new_neighborhoods, color))
                return result
        result = dfs(0, 0, 0)
        if result == math.inf:
            return -1
        return result
