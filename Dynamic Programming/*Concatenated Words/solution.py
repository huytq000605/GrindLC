class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordDict = set()
        for word in words: wordDict.add(word)
        
        @lru_cache(None)
        def canForm(word):
            for i in range(1, len(word)):
                first = word[:i]
                second = word[i:]
                if first in wordDict and (second in wordDict or canForm(second)):
                    wordDict.add(second)
                    return True
            
            return False
        result = []
        for word in words: 
            if canForm(word): 
                result.append(word)
                
        return result