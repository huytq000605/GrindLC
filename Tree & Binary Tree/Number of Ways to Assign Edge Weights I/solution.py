class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        tree = [[] for _ in range(n)]
        for u, v in edges:
            tree[u-1].append(v-1)
            tree[v-1].append(u-1)
        depth = 0
        dq = deque([(0, -1)])
        while len(dq) > 0:
            ndq = deque()
            while len(dq) > 0:
                u, p = dq.popleft()
                for v in tree[u]:
                    if v == p: continue
                    ndq.append((v, u))
            dq = ndq
            depth += 1
        depth -= 1
        return (2**(depth-1)) % (10**9 + 7)
