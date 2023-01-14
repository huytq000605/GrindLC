class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        c1, c2 = Counter(word1), Counter(word2)
        d1, d2 = len(c1), len(c2)
        for l1, f1 in c1.items():
            for l2, f2 in c2.items():
                nd1, nd2 = d1, d2
                if l1 != l2:
                    if f1 == 1: nd1 -= 1
                    if f2 == 1: nd2 -= 1
                    if c1[l2] == 0: nd1 += 1
                    if c2[l1] == 0: nd2 += 1
                
                if nd1 == nd2:
                    return True
        return False
