class WordFilter:

    def __init__(self, words: List[str]):
        trie = {}
        def insert(word, idx):
            current = trie
            for l in word:
                if l not in current:
                    current[l] = {}
                current = current[l]
                current['idx'] = idx
            
        for idx, word in enumerate(words):
            long = word + "_" + word
            for i in range(len(word)):
                insert(long[i:], idx)
        self.trie = trie
                
            

    def f(self, prefix: str, suffix: str) -> int:
        long = suffix + "_" + prefix
        current = self.trie
        for l in long:
            if l not in current:
                return -1
            current = current[l]
        return current['idx']


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
