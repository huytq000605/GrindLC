class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        current = self.trie
        for l in word:
            if l not in current:
                current[l] = {}
            current = current[l]
        current["word"] = True

    def search_in_trie(self, word, idx, current):
        if idx == len(word):
            if "word" in current:
                return True
            return False
        if word[idx] == ".":
            for key in current.keys():
                if key == "word": continue
                if self.search_in_trie(word, idx + 1, current[key]):
                    return True
            return False
        else:
            if word[idx] not in current:
                return False
            return self.search_in_trie(word, idx + 1, current[word[idx]])
    
    def search(self, word: str) -> bool:
        return self.search_in_trie(word, 0, self.trie)
                    


# Your WordDictionary object will beinstantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word) 
