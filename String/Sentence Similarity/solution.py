class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        n, m = len(sentence1), len(sentence2)
        if n != m:
            return False
        similars = defaultdict(dict)
        for w1, w2 in similarPairs:
            similars[w1][w2] = True
            similars[w2][w1] = True
        
        for i in range(n):
            w1, w2 = sentence1[i], sentence2[i]
            if w1 != w2 and w2 not in similars[w1]:
                    return False
        return True
                
            
