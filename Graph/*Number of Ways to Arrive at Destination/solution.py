import math
from heapq import *

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for i in range(n)]
        MOD = 1e9 + 7
        for road in roads:
            graph[road[0]].append([road[1], road[2]])
            graph[road[1]].append([road[0], road[2]])
        ways = [0 for i in range(n)]
        distance = [math.inf for i in range(n)]
        ways[0] = 1
        distance[0] = 0
        queue = [[0,0]]
        while queue:
            currDist, node = heappop(queue)
            if node == n-1:
                return ways[node]
            for nextNode, far in graph[node]:
                nextDist = far + currDist
                if nextDist < distance[nextNode]:
                    distance[nextNode] = nextDist
                    ways[nextNode] = ways[node]
                    ways[nextNode] = int(ways[nextNode] % MOD)
                    heappush(queue, [nextDist, nextNode])
                elif nextDist == distance[nextNode]:
                    ways[nextNode] += ways[node]
                    ways[nextNode] = int(ways[nextNode] % MOD)
                    
        return 0
                
                