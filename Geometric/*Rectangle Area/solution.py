class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        left = max(ax1, bx1)
        right = min(ax2, bx2)
        top = min(ay2, by2)
        down = max(ay1, by1)
        overlap = 0
        if left < right and down < top:
            overlap = (right - left) * (top - down)
        return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1) - overlap
