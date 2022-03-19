class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for u, v in tickets:
            graph[u].append(v)
        
        for u in graph.keys():
            graph[u].sort(reverse = True)
        
        path = []
        def dfs(u):
            if u in graph:
                while graph[u]:
                    v = graph[u].pop()
                    dfs(v)
            path.append(u)
        
        dfs("JFK")
        return path[::-1]