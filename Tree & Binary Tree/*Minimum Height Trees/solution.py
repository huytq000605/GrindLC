from collections import *
from typing import *

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [set() for i in range(n)]
        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)
        
        queue = deque()
        seen = set()
        
        for i in range (n):
            if len(graph[i]) <= 1:
                seen.add(i)
                queue.append(i)
        
        while n - len(seen) + len(queue) > 2:
            nextQueue = deque()
            while queue:
                node = queue.popleft()
                for nextNode in graph[node]:
                    if nextNode in seen: continue
                    graph[nextNode].remove(node)
                    if len(graph[nextNode]) == 1:
                        seen.add(nextNode)
                        nextQueue.append(nextNode)
            queue = nextQueue
        
        return queue
                