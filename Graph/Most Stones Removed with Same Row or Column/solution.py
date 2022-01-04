class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows = defaultdict(set)
        cols = defaultdict(set)
        island = 0
        for r, c in stones:
            rows[r].add((r,c))
            cols[c].add((r,c))
        seenRow = set()
        seenCol = set()
        
        def dfs(r, c):
            for nr, nc in rows[r]:
                if nr not in seenRow or nc not in seenCol:
                    seenRow.add(nr)
                    seenCol.add(nc)
                    dfs(nr, nc)
            
            for nr, nc in cols[c]:
                if nr not in seenRow or nc not in seenCol:
                    seenRow.add(nr)
                    seenCol.add(nc)
                    dfs(nr, nc)
        
        for r, c in stones:
            if r not in seenRow and c not in seenCol:
                seenRow.add(r)
                seenCol.add(c)
                island += 1
                dfs(r, c)
    
        return len(stones) - island
                
