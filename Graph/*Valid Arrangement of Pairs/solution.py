class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        degree = Counter()
        
        for u, v in pairs:
            graph[u].append(v)
            degree[u] += 1
            degree[v] -= 1
        
        start = pairs[0][0]
        for u in degree.keys():
            if degree[start] < degree[u]:
                start = u
        
        result = []
        def dfs(u):
            nonlocal result
            if u in graph:
                while graph[u]:
                    v = graph[u].pop()
                    dfs(v)
                    result.append([u, v])
            
        dfs(start)
        return result[::-1]