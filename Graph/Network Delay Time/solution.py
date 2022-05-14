class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        pq = [(0, k)]
        seen = set()
        while pq:
            t, u = heappop(pq)
            if u in seen:
                continue
            seen.add(u)
            if len(seen) == n:
                return t
            for v, w in graph[u]:
                if v not in seen:
                    heappush(pq, (t + w, v))
        return -1