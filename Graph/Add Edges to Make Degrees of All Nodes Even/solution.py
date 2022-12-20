class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        graph = [set() for i in range(n)]
        for u, v in edges:
            graph[u-1].add(v-1)
            graph[v-1].add(u-1)
        
        odds = []
        for u, adjs in enumerate(graph):
            if len(adjs) % 2: odds.append(u)
        
        if len(odds) > 4 or len(odds) % 2 == 1:
            return False
        
        # 2 4
        if len(odds) == 2:
            if odds[0] not in graph[odds[1]]:
                return True
            for u in range(n):
                if u != odds[0] and u != odds[1] and odds[0] not in graph[u] and odds[1] not in graph[u]:
                    return True
            return False
        
        if len(odds) == 4:
            a, b, c, d = odds
            if a not in graph[b] and c not in graph[d]:
                return True
            if a not in graph[c] and b not in graph[d]:
                return True
            if a not in graph[d] and b not in graph[c]:
                return True
            return False
            
        
        
        return True
        
