class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        walls_set = set([(r,c) for r, c in walls])
        guards_set = set([(r, c) for r, c in guards])
        
        guarded = set()
        dirs = [(0,1), (1,0), (0, -1), (-1, 0)]
        for r, c in guards:
            for d in dirs:
                cr, cc = r, c
                while True:
                    cr, cc = cr + d[0], cc + d[1]
                    if cr < 0 or cc < 0 or cr >= m or cc >= n or (cr, cc) in walls_set or (cr, cc) in guards_set:
                        break
                    if (cr, cc) not in guarded:
                        guarded.add((cr, cc))
        
        return m * n - len(walls_set) - len(guards_set) - len(guarded)