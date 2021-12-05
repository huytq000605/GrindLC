from collections import deque
from typing import *

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set()
        for word in wordList:
            words.add(word)
        
        if endWord not in wordList:
            return 0
        
        seen = set()
        queue = deque([[beginWord, 1]])
        
        while queue:
            word, step = queue.popleft()
            if word == endWord:
                return step
            for i in range(len(word)):
                for charCode in range(ord('a'), ord('z') + 1):
                    nextWord = word[:i] + chr(charCode) + word[i + 1:]
                    if nextWord in words and nextWord not in seen:
                        seen.add(nextWord)
                        queue.append([nextWord, step + 1])
        return 0