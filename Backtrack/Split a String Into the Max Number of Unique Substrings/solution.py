from typing import Set

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def split(start: int, hashset: Set) -> int:
            nonlocal s
            if start == len(s):
                return len(hashset)
            result = 0
            for i in range(start, len(s)):
                beUsedString = s[start: i + 1]
                if beUsedString not in hashset:
                    hashset.add(beUsedString)
                    result = max(result, split(i + 1, hashset))
                    hashset.remove(beUsedString)
            return result
        return split(0, set())
                    