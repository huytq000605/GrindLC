class Solution:
    def partitionString(self, s: str) -> int:
        freq = [0 for i in range(26)]
        result = 0
        for c in s:
            c = ord(c) - ord('a')
            if freq[c] > 0:
                freq = [0 for i in range(26)]
                result += 1
            freq[c] += 1
        return result + 1 # last partition
