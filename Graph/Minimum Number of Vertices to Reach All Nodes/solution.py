class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_deg = [0 for _ in range(n)]
        for u, v in edges:
            in_deg[v] += 1
        result = []
        for u in range(n):
            if not in_deg[u]:
                result.append(u)
        return result
        
