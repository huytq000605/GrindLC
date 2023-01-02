class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cnt = 0
        n = len(word)
        for c in word:
            if c.isupper():
                cnt += 1
        return cnt == 0 or (word[0].isupper() and (cnt == n or cnt == 1))
    
