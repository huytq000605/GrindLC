class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []
        for word in words:
            for w in word.split(separator):
                if w: result.append(w)
        return result
