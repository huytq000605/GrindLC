class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        result = []
        for r in range(m):
            for c in range(n):
                if land[r][c] == 0: continue
                r2, c2 = r, c
                while r2 < m and land[r2][c2]: r2 += 1
                r2 -= 1
                while c2 < n and land[r2][c2]: c2 += 1
                c2 -= 1
                result.append([r, c, r2 , c2])
                for fr in range(r, r2+1):
                    for fc in range(c, c2+1):
                        land[fr][fc] = 0
        return result
