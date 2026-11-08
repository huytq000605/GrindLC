class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        queries = sorted([(query, i) for i, query in enumerate(queries)])
        result = [0 for _ in range(len(queries))]
        logs.sort(key = lambda e: e[1])
        stored = deque()
        i = 0
        d = defaultdict(int)
        for query, idx in queries:
            while i < len(logs) and logs[i][1] <= query:
                server_id, t = logs[i]
                stored.append((server_id, t))
                d[server_id] += 1
                i += 1
            
            while stored and query - x > stored[0][1]:
                server_id, _ = stored.popleft()
                d[server_id] -= 1
                if d[server_id] == 0:
                    d.pop(server_id)
            result[idx] = n - len(d)
        return result
