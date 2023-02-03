class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        letters = dict()
        for i, c in enumerate(order):
            letters[c] = i
        n = len(words)
        
        def is_sort(w1, w2):
            for j in range(min(len(w1), len(w2))):
                if letters[w1[j]] < letters[w2[j]]:
                    return True
                elif letters[w1[j]] > letters[w2[j]]:
                    return False
            if len(w1) > len(w2):
                return False
            return True
        
        for i in range(1, n):
            w1, w2 = words[i-1], words[i]
            if not is_sort(w1, w2): return False
        return True
    
    
        
