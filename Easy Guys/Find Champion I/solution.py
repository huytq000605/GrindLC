class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for a in range(n):
            champion = True
            for b in range(n):
                if a == b: continue
                if not grid[a][b]:
                    champion = False
                    break
            if champion: return a
        return -1
