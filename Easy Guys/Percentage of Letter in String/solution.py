class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        freq = 0
        for l in s:
            if l == letter:
                freq += 1
        return freq * 100 // len(s)