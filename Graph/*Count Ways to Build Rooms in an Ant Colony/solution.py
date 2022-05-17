class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        n = len(prevRoom)
        graph = [[] for i in range(n)]
        count_child = [0 for i in range(n)]
        facts = [1 for i in range(n + 1)]
        modular_inverse = [1 for i in range(n+1)]
        MOD = 10**9 + 7
        
        for node, parent in enumerate(prevRoom):
            if node == 0:
                continue
            graph[parent].append(node)
            facts[node] = (facts[node - 1] * node) % MOD
            modular_inverse[node] = pow(facts[node], MOD - 2, MOD)
        
        def dfs(node):
            count = 0
            for children in graph[node]:
                count += dfs(children) + 1
            count_child[node] = count
            return count
        
        dfs(0)
        # nCa * (n-a)Cb * (n-a-b)Cc * (n-a-b-c)Cd
        # n! * (n-a)! * (n-a-b)! * (n-a-b-c)!
        # a!b!c!d!*(n-a)!*(n-a-b)!*(n-a-b-c)!
        # n!/(a!b!c!d!)
        
        def dfs2(node):
            result = facts[count_child[node]]
            for child in graph[node]:
                result *= dfs2(child)
                result *= modular_inverse[count_child[child] + 1]
            result %= MOD
            return result
        
        return dfs2(0)