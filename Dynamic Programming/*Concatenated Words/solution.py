class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        
        @cache
        def can_form(word):
            for i in range(len(word)):
                pref = word[:i]
                suff = word[i:]
                if pref in words and (suff in words or can_form(suff)):
                    return True
            return False
        
        return [word for word in words if can_form(word)]
