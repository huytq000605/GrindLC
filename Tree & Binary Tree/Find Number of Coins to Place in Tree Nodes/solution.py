class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        n = len(edges) + 1
        trees = [[] for _ in range(n)]
        for u, v in edges:
            trees[u].append(v)
            trees[v].append(u)
        
        coins = [0 for _ in range(n)] 
        def dfs(u, p):
            max_heap, min_heap = [-cost[u]], [cost[u]]
            for v in trees[u]:
                if v == p: continue
                child_max_heap, child_min_heap = dfs(v, u)
                for c in child_max_heap:
                    heappush(max_heap, c)
                    if len(max_heap) > 3:
                        heappop(max_heap)
                
                for c in child_min_heap:
                    heappush(min_heap, c)
                    if len(min_heap) > 3:
                        heappop(min_heap)

            if len(min_heap) < 3:
                coins[u] = 1
            else:
                # heap doesn't sort internally
                costs = ([*sorted(-c for c in max_heap), *sorted(min_heap)])
                
                coins[u] = max(0, costs[0] * costs[1] * costs[-1], costs[-1] * costs[-2] * costs[-3])
            return max_heap, min_heap
        dfs(0, -1)
        return coins                
                    
                
