class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        @cache
        def dfs(i, j, k):
            if i >= j:
                return 0
            if k == 1:
                mid = i + (j - i) // 2
                return sum([abs(houses[l] - houses[mid]) for l in range(i, j+1)])
            else:
                result = math.inf
                for l in range(i, j + 1):
                    result = min(result, dfs(i, l, 1) + dfs(l+1, j, k-1))
                return result
        return dfs(0, len(houses) - 1, k)
