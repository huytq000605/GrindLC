class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def mask_word(word):
            result = 0
            for l in word:
                result |= 1 << (ord(l) - ord("a"))
            return result
        
        word_dict = dict()
        for word in words:
            word_dict[word] = mask_word(word)
        
        result = 0
        
        for i in range(len(words)):
            for j in range(i, len(words)):
                if word_dict[words[i]] & word_dict[words[j]] == 0:
                    result = max(result, len(words[i]) * len(words[j]))
        return result