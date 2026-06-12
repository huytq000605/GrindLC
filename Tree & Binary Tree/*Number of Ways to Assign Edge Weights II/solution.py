class Solution:
    MOD = 10**9 + 7
    def pow_mod(self, a, b):
        result = 1
        while b:
            if b & 1: 
                result = (result * a) % self.MOD
            a = (a * a) % self.MOD
            b >>= 1
        return result


    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        # 17 = ceil(log2(10^5))
        LOG = 18
        
        n = len(edges) + 1
        tree = [[] for _ in range(n)]
        for u, v in edges:
            u = u-1
            v = v-1
            tree[u].append(v)
            tree[v].append(u)
        # parents
        ps = [[-1  for _ in range(LOG)] for _ in range(n)]
        # depth
        ds = [-1 for _ in range(n)]
        dq = deque([(0, -1)])
        depth = 0
        while len(dq) > 0:
            for i in range(len(dq)):
                u, p = dq.popleft()
                ps[u][0] = p
                for j in range(1, LOG):
                    ps[u][j] = ps[ps[u][j-1]][j-1]
                ds[u] = depth
                for v in tree[u]:
                    if v == p: continue
                    dq.append((v, u))
            depth += 1
        
        result = []
        for u, v in queries:
            u, v = u-1, v-1
            if u == v:
                result.append(0)
                continue
            s = 0
            if ds[v] < ds[u]:
                u, v = v, u
            if ds[v] > ds[u]:
                diff = ds[v] - ds[u]
                s += diff
                for i in range(LOG):
                    if diff & (1 << i):
                        v = ps[v][i]
            if u != v:
                for i in range(LOG-1, -1, -1):
                    if ps[u][i] != ps[v][i]:
                        s += 1 << (i+1)
                        u = ps[u][i]
                        v = ps[v][i]
                u = ps[u][0]
                v = ps[v][0]
                s += 2
            result.append(self.pow_mod(2, s-1))
        return result
