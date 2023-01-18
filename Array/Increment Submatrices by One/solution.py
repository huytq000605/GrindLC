class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        result = [[0 for _ in range(n)] for _ in range(n)]
        for r1, c1, r2, c2 in queries:
            for r in range(r1, r2+1):
                result[r][c1] += 1
                if c2 + 1 < n:
                    result[r][c2+1] -= 1
        for r in range(n):
            cur = 0
            for c in range(n):
                cur += result[r][c]
                result[r][c] = cur
        return result
                 
                
