class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        nwords = [0 for _ in range(n+1)]
        for i, word in enumerate(words):
            nwords[i+1] = nwords[i]
            if word[0] in "ueoai" and word[-1] in "ueoai":
                nwords[i+1] += 1
        result = []
        for l, r in queries:
            result.append(nwords[r+1] - nwords[l])
        return result
