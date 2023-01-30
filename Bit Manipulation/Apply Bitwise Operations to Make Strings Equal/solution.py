class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        # (1,1) -> (1, 0)
        # (1, 0) -> (1, 1)
        # (0, 1) -> (1, 1)
        # (0, 0) -> (0, 0)
        # We can change a string to anything except all zero with at least 1
        return True if max(s) == max(target) else False
