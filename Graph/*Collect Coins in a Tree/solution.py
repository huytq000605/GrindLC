class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        graph = [set() for _ in range(n)]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        q = deque()
        for u in range(n):
            if len(graph[u]) == 1:
                q.append(u)
                
        # clear all the subtree without coins and find all leafs after
        leafs = deque()
        while q:
            u = q.popleft()
            if not coins[u]:
                if graph[u]:
                    v = graph[u].pop()
                    graph[v].remove(u)
                    if len(graph[v]) == 1:
                        q.append(v)
                n -= 1
            else:
                leafs.append(u)

        # clear 2 levels from leafs
        for _ in range(2):
            for _ in range(len(leafs)):
                u = leafs.popleft()
                n -= 1
                if graph[u]: 
                    v = graph[u].pop()
                    graph[v].remove(u)
                    if len(graph[v]) == 1:
                        leafs.append(v)
        return max(0, (n-1)*2)
        
            
                
