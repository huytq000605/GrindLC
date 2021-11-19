class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        result = [0] * len(puzzles)
        def mask_word(word):
            mask = 0
            for l in word:
                mask |= 1 << (ord(l) - ord("a"))
            return mask
        
        freq = {}
        for word in words:
            mask = mask_word(word)
            freq[mask] = freq.get(mask, 0) + 1
        
        for i, puzzle in enumerate(puzzles):
            firstLetter = mask_word(puzzle[0])
            mask = mask_word(puzzle)
            subMask = mask
            res = 0
            while subMask > 0:
                if subMask & firstLetter:
                    res += freq[subMask]
                subMask = (subMask - 1) & mask
            result[i] = res
        return result