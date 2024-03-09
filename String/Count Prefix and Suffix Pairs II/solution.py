class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        trie = dict()
        def insert(trie, word):
            n = len(word)
            matched = 0
            for i in range(n):
                c1, c2 = word[i], word[n-1-i]
                if c1 not in trie: trie[c1] = dict()
                trie = trie[c1]
                matched += trie.get('count', 0)
                if c2 not in trie: trie[c2] = dict()
                trie = trie[c2]
                matched += trie.get('count', 0)
            trie['count'] = trie.get('count', 0) + 1
            return matched
        
        result = 0
        for word in words:
            result += insert(trie, word)
        return result
