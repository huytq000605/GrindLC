class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for i, (u, v, w) in enumerate(edges):
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        def dijkstra(start, skip_negative):
            ds = [math.inf for _ in range(n)]
            parent = dict()
            ds[start] = 0
            pq = [(0, start)]
            while pq:
                s, u = heappop(pq)
                for v, w in graph[u]:
                    if w == -1:
                        if skip_negative:
                            continue
                        else:
                            w = 1
                    if s + w < ds[v]:
                        ds[v] = s+w
                        parent[v] = u
                        heappush(pq, (s + w, v))
            return ds, parent
        
        dR, _ = dijkstra(destination, True)
        # If we have a way that cost < target without using any to be modified edge
        if dR[source] < target: return []
        d, p = dijkstra(source, False)
        # If we set all modified edge = 1, the min cost > target
        if d[destination] > target: return []

        # Find the path we're gonna use
        path = [destination]
        v = destination
        while v != source:
            u = p[v]
            path.append(u)
            v = u
        path = path[::-1]

        # Remap the edge for easier using
        edges = {(min(u, v), max(u, v)): w for u, v, w in edges}

        walked = 0
        for i in range(len(path) - 1):
            u, v = path[i], path[i+1]
            e = (min(u, v), max(u, v))
            if edges[e] == -1:
                # we also need to care about the path which is not our path
                # s = walked + w(u, v) + dR[v]
                # if we set w(u, v) to low, that will make other path is the shorest path
                edges[e] = max(target - dR[v] - walked, 1)
            walked += edges[e]
        
        return [[u, v, w] if w > 0 else [u, v, 2*(10**9)] for (u, v), w in edges.items()]
