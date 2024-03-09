class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def is_pref_and_suf(w1, w2):
            if len(w1) > len(w2): return False
            i = 0
            while i < len(w1) and w1[i] == w2[i]:
                i += 1
            if i < len(w1): return False
            i = len(w1) - 1
            j = len(w2) - 1
            while i >= 0 and w1[i] == w2[j]:
                i -= 1
                j -= 1
            return i < 0
                
        n = len(words)
        result = 0
        for i in range(n):
            for j in range(i+1, n):
                if is_pref_and_suf(words[i], words[j]):
                    result += 1
        return result
