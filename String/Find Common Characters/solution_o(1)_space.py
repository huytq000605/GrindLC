class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
        for c in range(26):
            ch = chr(ord('a') + c)
            count = math.inf
            for word in words:
                count = min(count, word.count(ch))
            result += count * ch
        return result
