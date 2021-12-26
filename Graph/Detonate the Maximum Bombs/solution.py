class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        ex = [[] for i in range(n)]
        for i, b1 in enumerate(bombs):
            for j, b2 in enumerate(bombs):
                if i == j:
                    continue
                x1, y1, r1 = b1
                x2, y2, r2 = b2
                if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r1**2:
                    ex[i].append(j)
        def dfs(pos, seen):
            result = 1
            for nextPos in ex[pos]:
                if nextPos not in seen:
                    seen.add(nextPos)
                    result += dfs(nextPos, seen)
            return result
        
        result = 0
        for i in range(n):
            result = max(result, dfs(i, set([i])))
        return result