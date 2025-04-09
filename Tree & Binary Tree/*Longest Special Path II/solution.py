class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        n = len(edges) + 1
        tree = [[] for _ in range(n)]
        for u, v, w in edges:
            tree[u].append((v, w))
            tree[v].append((u, w))
            
        prefix = [0]
        last = defaultdict(lambda: -1)
        result = [0, 0]
        last[nums[0]] = 0
        # i1, i2 is top2 depth that we could stay (i2 < i1)
        # maintaining top2 because we could allow one duplicate in the path.
        def dfs(u, p, i1, i2):
            nonlocal result
            length = prefix[-1] - prefix[i2+1]
            if length > result[0]:
                result = [length, len(prefix) - (i2+1)]
            elif length == result[0]:
                result[1] = min(result[1], len(prefix) - (i2+1))
                
            for v, w in tree[u]:
                if v == p: continue
                ni1 = max(i1, last[nums[v]])
                ni2 = max(min(i1, last[nums[v]]), i2)
                
                old_last = last[nums[v]]
                last[nums[v]] = len(prefix)
                prefix.append(prefix[-1] + w)
                    
                dfs(v, u, ni1, ni2)
                
                prefix.pop()
                last[nums[v]] = old_last

        dfs(0, -1, -1, -1)
        return result
            
            
                
                
