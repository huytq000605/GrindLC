class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        result = []
        count = [0 for i in range(n + 1)]
        shared = [Counter() for i in range(n + 1)]
        
        for u, v in edges:
            if u > v:
                u, v = v, u
            count[u] += 1
            count[v] += 1
            shared[u][v] += 1
        
        sorted_count = sorted(count)
            
        for query in queries:
            ans = 0
            i, j = 1, n
            while i < j:
                if sorted_count[i] + sorted_count[j] > query:
                    ans += j - i
                    j -= 1
                else:
                    i += 1
            
            for u in range(1, n+1):
                for v, uv in shared[u].items():
                    if count[u] + count[v] > query and count[u] + count[v] - shared[u][v] <= query:
                        ans -= 1
            result.append(ans)
        return result