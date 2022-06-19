class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = {}
        for word in products:
            current = trie
            for l in word:
                if l not in current:
                    current[l] = {}
                    current[l]['words'] = []
                current = current[l]
                current['words'].append(word)
        result = []
        for l in searchWord:
            if not trie or l not in trie:
                trie = None
                result.append([])
            else:
                trie = trie[l]
                result.append(trie['words'][:3])
        return result
