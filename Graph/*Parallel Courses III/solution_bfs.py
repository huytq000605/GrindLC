class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        ind = [0 for _ in range(n)]
        depends = [[] for _ in range(n)]
        for u, v in relations:
            u, v = u-1, v-1
            ind[v] += 1
            depends[u].append(v)
        
        dq = deque()
        ds = [0 for _ in range(n)]
        for u in range(n):
            if ind[u] == 0:
                dq.append(u)
        
        while dq:
            u = dq.popleft()
            ds[u] += time[u]
            for v in depends[u]:
                ind[v] -= 1
                ds[v] = max(ds[v], ds[u])
                if ind[v] == 0:
                    dq.append(v)
        return max(ds)
