class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m, n = len(picture), len(picture[0])
        rs, cs = [0 for _ in range(m)], [0 for _ in range(n)]
        for r in range(m):
            for c in range(n):
                if picture[r][c] == 'B':
                    rs[r] += 1
                    cs[c] += 1
        
        result = 0
        for r in range(m):
            for c in range(n):
                if picture[r][c] == 'B' and rs[r] == 1 and cs[c] == 1:
                    result += 1
        return result
