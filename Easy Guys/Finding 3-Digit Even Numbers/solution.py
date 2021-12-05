from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count = Counter()
        for digit in digits:
            count[digit] += 1
        
        result = []
        for i in range(1, 10):
            for j in range(0, 10):
                for k in range(0, 10, 2):
                    needI = 1
                    needJ = 1
                    needK = 1
                    if j == i:
                        needJ += 1
                    if k == j:
                        needK += 1
                    if k == i:
                        needK += 1
                    if count[i] >= needI and count[j] >= needJ and count[k] >= needK:
                        result.append(i*100 + j*10 + k)
        return result
                        