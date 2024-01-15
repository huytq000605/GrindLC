class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        offset = ord('a')
        indexes = [0 for _ in range(26)]
        for i, c in enumerate(keyboard):
            indexes[ord(c) - offset] = i
        
        idx = 0
        result = 0
        for c in word:
            next_idx = indexes[ord(c) - offset]
            result += abs(next_idx - idx)
            idx = next_idx
        return result
