class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0 for _ in range(n)]
        for u, v in edges:
            indegree[v] += 1
        
        result = -1
        for u in range(n):
            if indegree[u] == 0:
                if result == -1: result = u
                else: return -1
        return result
