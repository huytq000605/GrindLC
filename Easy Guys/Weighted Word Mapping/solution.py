class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = ""
        for word in words:
            s = 0
            for c in word:
                s += weights[ord(c) - ord('a')]
            result += chr(25 - (s%26) + ord('a'))
        return result
