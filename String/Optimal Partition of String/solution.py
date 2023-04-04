class Solution:
    def partitionString(self, s: str) -> int:
        mask = 0
        result = 0
        for c in s:
            c = ord(c) - ord('a')
            if (mask >> c) & 1:
                result += 1
                mask = 0
            mask |= (1<<c)
        return result + 1 # last partition
