class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        seen = [[math.inf for j in range(1 << n)] for i in range(n)]
        
        queue = deque()
        
        for node in range(n):
            queue.append([node, 1 << node, 0])
            
        while queue:
            node, states, step = queue.popleft()
            if states == (1<<n) - 1:
                return step
            for nextNode in graph[node]:
                nextStates = states | (1 << nextNode)
                if seen[nextNode][nextStates] > step + 1:
                    seen[nextNode][nextStates] = step + 1
                    queue.append([nextNode, nextStates, step + 1])
        return -1