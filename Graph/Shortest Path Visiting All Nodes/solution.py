class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        queue = deque()
        n = len(graph)
        for i in range(n):
            queue.append((i, 1 << i, 0))
        MEET_ALL = (1<<n) - 1
        seen = [[math.inf for j in range(MEET_ALL + 1)] for i in range(n)]
        while queue:
            current, mask, step = queue.popleft()
            for next_node in graph[current]:
                next_mask = mask | (1<<next_node)
                if next_mask == MEET_ALL:
                    return step + 1
                if seen[next_node][next_mask] > step + 1:
                    seen[next_node][next_mask] = step + 1
                    queue.append((next_node, next_mask, step + 1))
        
        return 0
