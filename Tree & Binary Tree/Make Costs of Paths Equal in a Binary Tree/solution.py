class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        leaf_threshold = n // 2 
        def dfs(u, s):
            nonlocal leaf_threshold, cost
            s += cost[u]
            # Find cost to go to every leaf nodes
            if u >= leaf_threshold:
                cost[u] = s
            else:
                dfs(u * 2 + 1, s)
                dfs(u * 2 + 2, s)
        dfs(0, 0)
        result = 0
        
        # Considering every 2 leaf nodes have same parent
        # Then merge them into 1 leaf nodes to the previous level
        start, end = leaf_threshold, n-1
        while start != end:
            for i in range(start, end+1, 2):
                result += abs(cost[i] - cost[i+1])
                cost[i // 2] = max(cost[i], cost[i+1])
            start = (start - 1) // 2
            end = (end - 2) // 2
        return result
            
        
        
        
