class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.prev = deque()
        for word in words:
            n = len(word)
            current = self.trie
            for i in range(n - 1, -1, -1):
                if word[i] not in current:
                    current[word[i]] = {}
                current = current[word[i]]
            current['isWord'] = True
            

    def query(self, letter: str) -> bool:
        self.prev.appendleft(letter)
        current = self.trie
        for l in self.prev:
            if l in current:
                current = current[l]
                if 'isWord' in current:
                    return True
            else:
                return False
        return False
        

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)