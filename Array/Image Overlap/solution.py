class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        i1, i2 = [], []
        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    i1.append((r, c))
                if img2[r][c] == 1:
                    i2.append((r, c))
        counter = Counter()
        for r1, c1 in i1:
            for r2, c2 in i2:
                counter[(r1 - r2, c1 - c2)] += 1
        if not counter:
            return 0
        return max(counter.values())
                
