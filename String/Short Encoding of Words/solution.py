class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key = len, reverse = True)
        result = 0
        seen = set()
        for word in words:
            if word in seen:
                continue
            for i in range(len(word)):
                seen.add(word[i:])
            result += len(word) + 1
        return result
