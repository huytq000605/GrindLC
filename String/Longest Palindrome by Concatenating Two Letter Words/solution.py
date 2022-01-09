from typing import *
from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        lookup = Counter()
        for word in words:
            lookup[word] += 1
        bonus = 0
        result = 0
        for word in lookup.keys():
            if lookup[word] == 0:
                continue
            rev = word[::-1]
            if rev == word:
                if lookup[word] % 2 == 1:
                    bonus = 2
                result += (lookup[word] // 2)*4
            elif rev != word and rev in lookup:
                plus = min(lookup[rev], lookup[word])
                result += plus * 4
                lookup[rev] = 0
                lookup[word] = 0
        return result + bonus