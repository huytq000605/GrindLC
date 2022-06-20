class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = [[] for i in range(n)]
        parents = [0 for i in range(n)]
        for u, v in edges:
            graph[u].append(v)
            parents[v] += 1
        
        result = 0
        queue = []
        seen = set()
        counts = [[0 for j in range(26)] for i in range(n)]
        
        for node in range(n):
            if parents[node] == 0:
                queue.append(node)
                seen.add(node)
                counts[node][ord(colors[node]) - ord('a')] = 1
                result = 1
        
        while queue:
            node = queue.pop()
            for next_node in graph[node]:
                if next_node in seen:
                    return -1
                letter = ord(colors[next_node]) - ord('a')
                for i in range(26):
                    if i == letter:
                        counts[next_node][i] = max(counts[next_node][i], counts[node][i] + 1)
                    else:
                        counts[next_node][i] = max(counts[next_node][i], counts[node][i])
                    result = max(result, counts[next_node][i])
                parents[next_node] -= 1
                if parents[next_node] == 0:
                    seen.add(next_node)
                    queue.append(next_node)
        
        if len(seen) != n:
            return -1
        return result