class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        word_set = set(words)
        result = 0
        @cache
        def dp(word):
            result = 1
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                if predecessor in word_set:
                    result = max(result, 1 + dp(predecessor))
            return result
        for word in words:
            result = max(dp(word), result)
        return result
