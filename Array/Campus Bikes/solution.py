class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distances = [[] for _ in range(2000)]
        for i, (x1, y1) in enumerate(workers):
            for j, (x2, y2) in enumerate(bikes):
                d = abs(x1-x2) + abs(y1-y2)
                distances[d].append((i, j))
        result = [-1 for _ in range(len(workers))]
        used_bikes = [0 for _ in range(len(bikes))]
        for d in range(2000):
            for i, j in distances[d]:
                if result[i] != -1: continue
                if used_bikes[j]: continue
                result[i] = j
                used_bikes[j] = 1
        return result
