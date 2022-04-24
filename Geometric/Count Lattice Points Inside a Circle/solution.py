class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        result = set()
        for xo, yo, r in circles:
            for x in range(xo - r, xo + r + 1):
                for y in range(yo - r, yo + r + 1):
                    if abs(xo - x)**2 + abs(yo - y)**2 <= r**2:
                        result.add((x, y))
        return len(result)