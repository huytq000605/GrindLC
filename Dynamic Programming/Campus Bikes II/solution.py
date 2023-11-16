class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        m = len(bikes)
        @cache
        def dfs(worker, mask):
            if worker >= len(workers):
                return 0
            x1, y1 = workers[worker]
            result = math.inf
            for bike in range(m):
                if (mask >> bike) & 1:
                    continue
                x2, y2 = bikes[bike]
                d = abs(x1 - x2) + abs(y1 - y2)
                next_mask = mask | (1 << bike)
                result = min(result, d + dfs(worker + 1, next_mask))
            return result
        return dfs(0, 0)
                 
