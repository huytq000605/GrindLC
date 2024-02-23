class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        counter = [0 for _ in range(n)]
        
        # This is a tree, no cycle, so there's only 1 way from u to d
        def dfs(u, d, p):
            nonlocal counter
            counter[u] += 1
            if u == d: return True
            for v in graph[u]:
                if v == p: continue
                if dfs(v, d, u):
                    return True
            counter[u] -= 1
            return False
        
        for u, v in trips:
            dfs(u, v, -1)
        
        @cache
        def get_price(u, p, halved):
            if halved:
                start = (price[u] // 2) * counter[u]
            else:
                start = price[u] * counter[u]
            
            result = start
            if halved:
                for v in graph[u]:
                    if v == p: continue
                    result += get_price(v, u, False)
            else:
                for v in graph[u]:
                    if v == p: continue
                    result += min(get_price(v, u, False), get_price(v, u, True))
            return result
        # Try all combinations to see which will give the best result
        # Half zero or not half zero will have all the combinations
        return min(get_price(0, -1, True), get_price(0, -1, False))
                
