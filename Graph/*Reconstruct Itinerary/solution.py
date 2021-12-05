class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        cities = set()
        freq = Counter()
        for start, end in tickets:
            cities.update([start, end])
            graph[start].append(end)
            freq[start] += 1
            freq[end] -= 1
        
        for key in graph.keys():
            graph[key] = sorted(graph[key], reverse = True)
        
        result = []
        def dfs(start):
            nonlocal result
            while graph[start]:
                nextStart = graph[start].pop()
                dfs(nextStart)
            result.append(start)
        dfs("JFK")
        return result[::-1]
                
            