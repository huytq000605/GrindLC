class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # (a, b) denotes the position of the white rook.
        # (c, d) denotes the position of the white bishop.
        # (e, f) denotes the position of the black queen.

        # rook and queen are in the same row and bishop is not in the middle
        if a == e and not (a == c and (b < d < f or b > d > f)): 
            return 1
        # rook and queen are in the same column and bishop is not in the middle
        if b == f and not (b == d and (a < c < e or a > c > e)):
            return 1
        # bishop and queen are in same diagonal and rook is not in the middle
        if c - d == e - f and not (a-b == c-d and (c < a < e or c > a > e)):
            return 1
        # bishop and queen are in same diagonal and rook is not in the middle
        if c + d == e + f and not (a + b == c + d and (c < a < e or c > a > e)):
            return 1
        return 2
