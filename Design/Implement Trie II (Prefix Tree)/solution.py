class Trie:

    def __init__(self):
        self.root = [dict()]

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur[0]:
                cur[0][c] = [dict(), 0, 0]
            cur = cur[0][c]
            cur[1] += 1
        cur[2] += 1
            
        
    def countWordsEqualTo(self, word: str) -> int:
        cur = self.root
        for c in word:
            if c not in cur[0]:
                return 0
            cur = cur[0][c]
        return cur[2]

    def countWordsStartingWith(self, prefix: str) -> int:
        cur = self.root
        for c in prefix:
            if c not in cur[0]:
                return 0
            cur = cur[0][c]
        return cur[1]

    def erase(self, word: str) -> None:
        cur = self.root
        for c in word:
            cur = cur[0][c]
            cur[1] -= 1
        cur[2] -= 1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
