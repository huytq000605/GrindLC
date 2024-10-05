class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowers = set()
        uppers = set()
        result = set()
        excluded = set()
        for c in word:
            if c in excluded: continue
            if c.isupper():
                if c.lower() in lowers: result.add(c)
                uppers.add(c)
            else:
                if c.upper() in uppers: 
                    excluded.add(c)
                    excluded.add(c.upper())
                    result.discard(c.upper())
                lowers.add(c)
        return len(result)
