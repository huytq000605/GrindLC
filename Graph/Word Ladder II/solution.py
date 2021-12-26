from typing import *
from collections import deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words = set()
        for word in wordList:
            words.add(word)
            
        if endWord not in wordList:
            return []
            
        minSteps = dict()
        
        queue = deque([[beginWord, 1, [beginWord]]])
        
        result = []
        while queue:
            word, step, path = queue.popleft()
            if word == endWord:
                result.append(path)
                continue
            for i in range(len(word)):
                for charCode in range(ord('a'), ord('z') + 1):
                    nextWord = word[:i] + chr(charCode) + word[i + 1:]
                    if nextWord in words and (nextWord not in minSteps or step + 1 <= minSteps[nextWord]):
                        minSteps[nextWord] = step + 1
                        queue.append([nextWord, step + 1, [*path, nextWord]])
        return result
                