class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        queue = deque([(beginWord, 1)])
        n = len(beginWord)
        while queue:
            word, step = queue.popleft()
            for i in range(n):
                for letter in map(chr, [ord('a') + i for i in range(26)]):
                    next_word = word[:i] + letter + word[i+1:]
                    if next_word in words:
                        if next_word == endWord:
                            return step + 1
                        words.remove(next_word)
                        queue.append((next_word, step + 1))
        return 0