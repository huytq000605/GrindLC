class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MAX_BIT = math.ceil(math.log2(n))
        # depths[u] = depth from root to u
        depths = [n+1 for _ in range(n)]
        # weights[u][w] = number of edge have weight `w` from root to u
        weights = [None for _ in range(n)]
        # binary lifting
        parent = [[-1 for _ in range(MAX_BIT + 1)] for _ in range(n)]
        
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        def dfs(u):
            nonlocal current_weight, depths, weights
            for v, w in graph[u]:
                if depths[v] < depths[u]: continue
                current_weight[w] += 1
                depths[v] = depths[u] + 1
                weights[v] = [*current_weight]
                parent[v][0] = u
                for bit in range(1, MAX_BIT + 1):
                    if parent[parent[v][bit-1]][bit-1] == -1: break
                    parent[v][bit] = parent[parent[v][bit-1]][bit-1]
                dfs(v)
                current_weight[w] -= 1
        # choose 0 as root, initialize current_weight, depths, weights
        current_weight = [0 for _ in range(27)]
        depths[0] = 0
        weights[0] = [*current_weight]
        dfs(0)
        
        def find_lca(u, v):
            if depths[u] > depths[v]:
                u, v = v, u
            # go to same depth
            depth_diff = depths[v] - depths[u]
            for bit in range(MAX_BIT + 1):
                if (depth_diff >> bit) & 1:
                    v = parent[v][bit]
                    
            # if u is ancestor
            if u == v:
                return u
            
            # find parent
            for bit in range(MAX_BIT, -1, -1):
                if parent[u][bit] != parent[v][bit]:
                    u, v = parent[u][bit], parent[v][bit]
            return parent[u][0]

        result = []
        for u, v in queries:
            lca = find_lca(u, v)
            # operations[i] = number of weight `i` on the way from u to v
            operations = [weights[u][w] + weights[v][w] - 2 * weights[lca][w] for w in range(27)]
            result.append(sum(operations) - max(operations))
        return result
