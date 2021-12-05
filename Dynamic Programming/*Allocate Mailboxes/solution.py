class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)
        
        @cache
        def dfs(start, end, k):
            if start >= end:
                return 0
            if k == 1:
				# All the houses use the same mailbox
				# Sum of minimum distance will be sum to median
                mid = start + (end - start) // 2
                diff = sum([abs(houses[i] - houses[mid]) for i in range(start, end + 1)])
                return diff
            else:
                result = math.inf
				# Try to split (i+1 to end) with a mailbox
                for i in range(start, end + 1):
                    result = min(result, dfs(start, i, k - 1) + dfs(i + 1, end, 1))
                return result
        return dfs(0, n - 1, k)