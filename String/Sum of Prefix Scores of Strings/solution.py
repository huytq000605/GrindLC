class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = dict()
        for word in words:
            cur = trie
            for c in word:
                if c not in cur:
                    cur[c] = dict()
                    cur[c]['count'] = 1
                else:
                    cur[c]['count'] += 1
                cur = cur[c]
        result = [0 for i in range(len(words))]
        for i, word in enumerate(words):
            cur = trie
            for c in word:
                cur = cur[c]
                result[i] += cur['count']
        return result
