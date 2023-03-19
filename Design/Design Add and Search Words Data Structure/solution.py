class WordDictionary:

    def __init__(self):
        self.trie = dict()
        

    def addWord(self, word: str) -> None:
        cur = self.trie
        for c in word:
            if c not in cur: cur[c] = dict()
            cur = cur[c]
        cur["is_word"] = True
    
    def dfs(self, word, idx, trie):
        for i in range(idx, len(word)):
            c = word[i]
            if c == ".":
                for key, next_trie in trie.items():
                    if key == "is_word": continue
                    if self.dfs(word, i + 1, next_trie): return True
                return False
            
            if c not in trie: return False
            trie = trie[c]
        return "is_word" in trie

    def search(self, word: str) -> bool:
        return self.dfs(word, 0, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
