class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse_graph = [[] for _ in range(n)]
        q = []
        result = []
        counter = Counter()
        for u in range(n):
            if not graph[u]:
                q.append(u)
                result.append(u)
            for v in graph[u]:
                reverse_graph[v].append(u)
        while q:
            v = q.pop()
            for u in reverse_graph[v]:
                counter[u] += 1
                if counter[u] == len(graph[u]):
                    result.append(u)
                    q.append(u)
            reverse_graph[v] = []
        return sorted(result)
