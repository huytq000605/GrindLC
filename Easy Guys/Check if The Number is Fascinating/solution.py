class Solution:
    def isFascinating(self, n: int) -> bool:
        n2 = n*2
        n3 = n*3
        s = str(n) + str(n2) + str(n3)
        counter = Counter(s)
        for d in range(1, 10):
            if counter[str(d)] != 1:
                return False
        if counter[str(0)] > 0:
            return False
        return True
