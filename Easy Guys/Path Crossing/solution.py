class Solution:
    def isPathCrossing(self, path: str) -> bool:
        ds = {
            "N": (0, 1),
            "S": (0, -1),
            "W": (-1, 0),
            "E": (1, 0)
        }
        r, c = 0, 0
        seen = set()
        seen.add((r, c))
        for d in path:
            dr, dc = ds[d]
            r, c = r + dr, c + dc
            if (r, c) in seen:
                return True
            seen.add((r, c))
        return False
        
