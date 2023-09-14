class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for u, v in tickets:
            graph[u].append(v)
        
        for u in graph.keys():
            graph[u].sort(reverse = True)
            
        result = []
        def dfs(u):
            while graph[u]:
                dfs(graph[u].pop())
            result.append(u)
        dfs("JFK")
        return result[::-1]
