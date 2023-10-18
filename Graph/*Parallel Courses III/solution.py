class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        depends = [[] for _ in range(n)]
        for u, v in relations:
            u, v = u-1, v-1
            depends[v].append(u)
        
        @cache
        def dfs(u):
            result = time[u]
            if depends[u]:
                result += max([dfs(v) for v in depends[u]])
            return result
    
        return max([dfs(u) for u in range(n)])
