class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        n = len(scores)
        top_3 = [[] for i in range(n)]
        for u in range(n):
            for v in graph[u]:
                heappush(top_3[u], (scores[v], v))
                if len(top_3[u]) > 3:
                    heappop(top_3[u])
        result = -1
        for u, v in edges:
            for _s, x in top_3[u]:
                if x == v:
                    continue
                for _s, z in top_3[v]:
                    if z == x or z == u:
                        continue
                    score = sum(scores[i] for i in (u,v,x,z))
                    result = max(result, score)
        
        return result