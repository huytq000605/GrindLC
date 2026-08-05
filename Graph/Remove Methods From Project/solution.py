class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)
        dq = deque([k])
        suspicious = [False for _ in range(n)]
        suspicious[k] = True
        while dq:
            u = dq.popleft()
            for v in graph[u]:
                if suspicious[v]: continue
                suspicious[v] = True
                dq.append(v)
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]: return [u for u in range(n)]
        return [u for u in range(n) if not suspicious[u]]
