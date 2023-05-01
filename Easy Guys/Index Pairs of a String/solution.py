class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        n = len(text)
        result = []
        for word in words:
            m = len(word)
            for i in range(n-m+1):
                if text[i:i+m] == word:
                    result.append([i, i+m-1])
        result.sort()
        return result
