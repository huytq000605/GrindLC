class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        indegree = [0 for _ in range(n)]
        for u, v in relations:
            graph[u-1].append(v-1)
            indegree[v-1] += 1
        
        s = deque()
        learn = 0
        for u in range(n):
            if not indegree[u]: 
                s.append(u)
                learn += 1
        
        result = 0
        while s:
            result += 1
            for _ in range(len(s)):
                u = s.popleft()
                for v in graph[u]:
                    indegree[v] -= 1
                    if not indegree[v]:
                        s.append(v)
                        learn += 1
        if learn != n:
            return -1
        return result
