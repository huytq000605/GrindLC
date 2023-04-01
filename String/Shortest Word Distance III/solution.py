class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        i1, i2 = -1, -1
        result = math.inf
        eq = word1 == word2
        for i, word in enumerate(wordsDict): 
            if word == word1:
                if eq and i1 > -1: result = min(result, i - i1)
                i1 = i
            if word == word2:
                i2 = i
            if not eq and i1 != -1 and i2 != -1:
                result = min(result, abs(i2 - i1))
        return result
