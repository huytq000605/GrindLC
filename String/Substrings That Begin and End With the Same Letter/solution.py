class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        seen = defaultdict(int)
        result = 0
        for c in s:
            seen[c] += 1
            result += seen[c]
        return result
