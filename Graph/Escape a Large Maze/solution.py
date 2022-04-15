class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        n = len(blocked)
        blocked = set(map(tuple, blocked))
        source = tuple(source)
        target = tuple(target)
        
        def not_valid(point):
            x, y = point
            if x < 0 or y < 0 or x >= 10**6 or y >= 10**6:
                return True
            return False
        
        def distance(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return abs(x1 - x2) + abs(y1 - y2)
        
        def dfs(current, target, source, seen):
            for d in dirs:
                nr, nc = current[0] + d[0], current[1] + d[1]
                next_point = (nr, nc)
                if not_valid(next_point) or next_point in seen or next_point in blocked:
                    continue
                seen.add(next_point)
                if distance(source, next_point) > n or next_point == target:
                    return True
                if dfs(next_point, target, source, seen):
                    return True
            return False
        
        
        return dfs(source, target, source, set([source])) and dfs(target, source, target, set([target]))