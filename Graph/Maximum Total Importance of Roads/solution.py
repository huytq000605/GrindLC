class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0 for _ in range(n)]
        for u, v in roads:
            degree[u] += 1
            degree[v] += 1
        degree.sort()
        result = 0
        for i in range(n):
            result += degree[i] * (i + 1)
        return result
