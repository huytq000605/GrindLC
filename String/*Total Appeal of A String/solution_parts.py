class Solution:
    def appealSum(self, s: str) -> int:
        last = [-1 for i in range(26)]
        n = len(s)
        result = 0
        # Count how many substring have c = s[i] as the first character `c` looking from the right to left
        # Look at 828. *Count Unique Characters of All Substrings of a Given String
        for i, l in enumerate(s):
            c = ord(l) - ord('a')
            result += ((last[c] - 1) + 1 + 1) * ( (i-1) - (last[c]+1) + 1 + 1)
            last[c] = i
        for c in range(26):
            result += ((last[c] - 1) + 1 + 1) * ( (n-1) - (last[c]+1) + 1 + 1)
        return result