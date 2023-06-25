class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        MOD = 10**9 + 7
        @cache
        def dfs(i, fuel):
            result = 0
            if i == finish: result += 1
            for j in range(n):
                if j == i: continue
                new_fuel = fuel - abs(locations[i] - locations[j])
                if new_fuel < 0: continue
                result = (result + dfs(j, new_fuel)) % MOD
            return result 
        return dfs(start, fuel)
