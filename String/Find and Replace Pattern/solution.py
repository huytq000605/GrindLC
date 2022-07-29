class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        n = len(pattern)
        result = []
        def match(w1, w2):
            w1_to_w2, w2_to_w1 = dict(), dict()
            for i in range(n):
                if w1[i] not in w1_to_w2 and w2[i] not in w2_to_w1:
                    w1_to_w2[w1[i]] = w2[i]
                    w2_to_w1[w2[i]] = w1[i]
                if w1[i] not in w1_to_w2 or w1_to_w2[w1[i]] != w2[i]:
                    return False
            return True

        for word in words:
            if match(word, pattern):
                result.append(word)
        return result
