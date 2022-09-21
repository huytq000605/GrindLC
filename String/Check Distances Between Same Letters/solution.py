class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        seen = [-1 for i in range(26)]
        for i, c in enumerate(s):
            c = ord(c) - ord('a')
            if seen[c] >= 0 and i - seen[c] - 1 != distance[c]:
                return False
            seen[c] = i
        return True
