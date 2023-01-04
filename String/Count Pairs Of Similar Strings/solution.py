class Solution:
    def similarPairs(self, words: List[str]) -> int:
        n = len(words)
        result = 0
        
        def similar(w1, w2):
            s1, s2 = set(w1), set(w2)
            if len(s1 | s2) == len(s1) == len(s2):
                return True
            return False
        
        for i in range(n):
            for j in range(i+1, n):
                if similar(words[i], words[j]):
                    result += 1
        return result
