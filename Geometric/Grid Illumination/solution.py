class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        rows = defaultdict(set)
        cols = defaultdict(set)
        dia1 = defaultdict(set)
        dia2 = defaultdict(set)
        dirs = [(0,1), (1,0), (-1,0), (0,-1), (-1,-1), (1, 1), (1, -1), (-1, 1), (0, 0)]
        
        for r, c in lamps:
            rows[r].add((r, c))
            cols[c].add((r, c))
            dia1[r-c].add((r, c))
            dia2[r+c].add((r, c))
        result = []
        for r, c in queries:
            # Should check if key in dict or not
            if len(rows[r]) > 0 or len(cols[c]) > 0 or len(dia1[r-c]) > 0 or len(dia2[r+c]) > 0:
                result.append(1)
            else:
                result.append(0)
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= n or nc >= n:
                    continue
                # Should check if key in dict or not
                rows[nr].discard((nr, nc))
                cols[nc].discard((nr, nc))
                dia1[nr - nc].discard((nr, nc))
                dia2[nr + nc].discard((nr, nc))
        return result