class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        tree = [[] for _ in range(n + 1)]
        for u, v in edges:
            u, v = u, v
            tree[u].append(v)
            tree[v].append(u)
        
        result = 0
        
        is_prime = [1 for _ in range(n + 1)]
        is_prime[1] = 0
        for num in range(2, n+1):
            if is_prime[num]:
                cur = num * num
                while cur <= n:
                    is_prime[cur] = 0
                    cur += num
        
        def dfs(u, p):
            nonlocal result
            total_ones, total_zeros = 0, 0
            for v in tree[u]:
                if v == p: continue
                ones, zeros = dfs(v, u)
                # from itself
                if is_prime[u]:
                    result += zeros
                else:
                    result += ones
                
                # as a bridge
                if is_prime[u]:
                    result += zeros * total_zeros
                else:
                    result += ones * total_zeros + zeros * total_ones
                total_ones += ones
                total_zeros += zeros
            
            if is_prime[u]:
                return total_zeros + 1, 0
            else:
                return total_ones, total_zeros + 1
        dfs(1, -1)
        return result
