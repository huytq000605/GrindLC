class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for i in range(n)]
        for u, v in edges:
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)
        
        # Make sure the graph is biparte
        # If it's not cycle: just label from 1 to n
        # If it's cycle with even length: just label with +1 -1
        # If it's cycle with odd length: cannot label idx
        def make_color(u, color):
            nonlocal groups
            for v in graph[u]:
                if colors[v] == color:
                    return False
                if colors[v] != -1:
                    continue
                groups[-1].append(v)
                colors[v] = 1 - color
                if not make_color(v, 1 - color):
                    return False
            return True

        groups = []
        colors = [-1 for i in range(n)]
        for i in range(n):
            if colors[i] != -1:
                continue
            groups.append([i])
            if not make_color(i, 0):
                return -1
        # Try to label from each starting point in a group
        def bfs(u):
            seen = set([u])
            q, nq = [u], []
            result = 0
            while q:
                result += 1
                while q:
                    u = q.pop()
                    for v in graph[u]:
                        if v in seen: continue
                        seen.add(v)
                        nq.append(v)
                q, nq = nq, q
            return result
        
        return sum(max(bfs(u) for u in group) for group in groups)
