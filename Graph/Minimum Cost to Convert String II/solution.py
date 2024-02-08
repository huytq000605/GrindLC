class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = defaultdict(list)
        lengths = set()
        for u, v, c in zip(original, changed, cost):
            graph[u].append((v, c))
            lengths.add(len(u))
            
        distances = defaultdict(lambda: defaultdict(lambda: math.inf))
        for start in original:
            distances[start][start] = 0
            pq = [(0, start)]
            while pq:
                d, u = heappop(pq)
                for v, c in graph[u]:
                    if d + c < distances[start][v]:
                        distances[start][v] = d + c
                        heappush(pq, (d + c, v))
        
        lengths = sorted(lengths)
        n = len(source)
        @cache
        def dfs(i):
            if i >= n:
                return 0
            result = math.inf
            if source[i] == target[i]:
                result = min(result, dfs(i+1))
            for length in lengths:
                if i + length - 1 >= n: break
                j = i + length - 1
                if source[i:j+1] in distances and target[i:j+1] in distances[source[i:j+1]]:
                    result = min(result, dfs(j+1) + distances[source[i:j+1]][target[i:j+1]])
            return result
        result = dfs(0)
        if result == math.inf:
            return -1
        return result
            
